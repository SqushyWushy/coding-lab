import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl

# Function to parse embedded data
def parse_embedded_data(text):
    if pd.isna(text):
        return {}
    lines = [line.strip() for line in text.split(';') if line.strip()]
    parsed = {}
    for line in lines:
        if ':' in line:
            try:
                key, value = line.split(':', 1)
                parsed[key.strip().lower()] = value.strip()
            except ValueError:
                pass
    return parsed

# Calculate session duration in minutes
def calculate_session_duration(row):
    try:
        start = pd.to_datetime(row['session start'], format='%I:%M %p')
        end = pd.to_datetime(row['session end'], format='%I:%M %p')
        return (end - start).total_seconds() / 60
    except:
        return None

# Calculate time difference in minutes
def calculate_time_difference(scheduled_time, actual_time):
    if pd.isna(scheduled_time) or pd.isna(actual_time):
        return None
    try:
        return (actual_time - scheduled_time).total_seconds() / 60
    except:
        return None

# Calculate when student departed (session end time)
def calculate_student_departure_time(row):
    try:
        if pd.isna(row['date']) or pd.isna(row['session end']):
            return None
        departure_time = pd.to_datetime(str(row['date']) + ' ' + str(row['session end']), errors='coerce')
        return departure_time
    except:
        return None

# Known name aliases for instructors
INSTRUCTOR_ALIASES = {
    'roxanne pirmoradi': 'roxanne roshan',
    'roxanne roshan': 'roxanne pirmoradi',
    # Add more known aliases as needed
}

# Fuzzy name matching function
def names_match(name1, name2, threshold=0.8):
    """Check if two names are similar enough to be considered a match"""
    if pd.isna(name1) or pd.isna(name2):
        return False
    
    name1_clean = str(name1).lower().strip()
    name2_clean = str(name2).lower().strip()
    
    # Check known aliases first
    if name1_clean in INSTRUCTOR_ALIASES and INSTRUCTOR_ALIASES[name1_clean] == name2_clean:
        return True
    if name2_clean in INSTRUCTOR_ALIASES and INSTRUCTOR_ALIASES[name2_clean] == name1_clean:
        return True
    
    # Exact match
    if name1_clean == name2_clean:
        return True
    
    # Check if one name is contained in the other
    if name1_clean in name2_clean or name2_clean in name1_clean:
        return True
    
    # Split names and check parts
    parts1 = name1_clean.split()
    parts2 = name2_clean.split()
    
    # Must have same number of name parts (first, last, etc.)
    if len(parts1) != len(parts2):
        # Try partial matching if different lengths
        shorter_parts = parts1 if len(parts1) <= len(parts2) else parts2
        longer_parts = parts2 if len(parts1) <= len(parts2) else parts1
        
        matches = 0
        for part in shorter_parts:
            for long_part in longer_parts:
                if part in long_part or long_part in part or similar_strings(part, long_part):
                    matches += 1
                    break
        return matches >= len(shorter_parts) * threshold
    
    # Same number of parts - check each part individually
    matches = 0
    for p1, p2 in zip(parts1, parts2):
        if p1 == p2 or p1 in p2 or p2 in p1 or similar_strings(p1, p2):
            matches += 1
    
    # Special case for common name variations (e.g., Roxanne Pirmoradi vs Roxanne Roshan)
    if matches >= 1 and len(parts1) == 2 and len(parts2) == 2:
        # If first names match, be more lenient with last names
        if parts1[0] == parts2[0]:
            # Check if last names start with same letter or have some similarity
            if parts1[1][0] == parts2[1][0] or similar_strings(parts1[1], parts2[1], 0.6):
                matches = len(parts1)  # Consider it a full match
    
    return matches >= len(parts1) * threshold

def similar_strings(s1, s2, similarity_threshold=0.8):
    """Check if two strings are similar using character-level similarity"""
    if not s1 or not s2:
        return False
    
    # Calculate character overlap ratio
    common_chars = sum(c1 == c2 for c1, c2 in zip(s1, s2))
    max_len = max(len(s1), len(s2))
    similarity = common_chars / max_len
    
    # Also check if most characters are the same (allowing for typos)
    if len(s1) == len(s2):
        return similarity >= similarity_threshold
    
    # For different lengths, be more lenient if the difference is small
    len_diff = abs(len(s1) - len(s2))
    if len_diff <= 2:  # Allow up to 2 character difference
        # Check longest common subsequence approach
        shorter = s1 if len(s1) <= len(s2) else s2
        longer = s2 if len(s1) <= len(s2) else s1
        
        # Count matching characters in order
        matching = 0
        j = 0
        for i in range(len(shorter)):
            while j < len(longer) and longer[j] != shorter[i]:
                j += 1
            if j < len(longer):
                matching += 1
                j += 1
        
        return matching / len(shorter) >= similarity_threshold
    
    return False

# Find instructor cleanup time - FIXED for multi-day data
def calculate_instructor_cleanup_time(instructor_name, df_checkin, df_timesheet, target_date):
    if df_timesheet is None:
        return None, None, None
    
    # Find instructor's timesheet for the target date with fuzzy name matching
    instructor_timesheet = None
    matched_timesheet_name = None
    
    for _, row in df_timesheet[df_timesheet['date'] == target_date].iterrows():
        if names_match(instructor_name, row['instructor name']):
            instructor_timesheet = df_timesheet[
                (df_timesheet['instructor name'] == row['instructor name']) & 
                (df_timesheet['date'] == target_date)
            ]
            matched_timesheet_name = row['instructor name']
            break
    
    if instructor_timesheet is None or instructor_timesheet.empty:
        return None, None, None
    
    # Get instructor clock out time
    clock_out_time = None
    if 'clock out' in instructor_timesheet.columns:
        clock_out_str = instructor_timesheet['clock out'].iloc[0]
        if pd.notna(clock_out_str):
            try:
                clock_out_time = pd.to_datetime(str(target_date) + ' ' + str(clock_out_str), errors='coerce')
            except:
                pass
    
    # CRITICAL FIX: Only get instructor's students for the SAME target_date
    instructor_students = df_checkin[
        (df_checkin['instructors'].str.contains(instructor_name, na=False)) &
        (df_checkin['date'] == target_date)  # Same day only!
    ]
    
    if instructor_students.empty:
        return clock_out_time, None, None
    
    # Calculate departure times for students on the same day
    instructor_students = instructor_students.copy()
    instructor_students['departure_time'] = instructor_students.apply(calculate_student_departure_time, axis=1)
    
    # COMPREHENSIVE FIX: Only consider students who:
    # 1. Left BEFORE the instructor clocked out, AND
    # 2. Did NOT work with multiple instructors (no handoffs)
    
    # First, get all students this instructor worked with
    valid_students_data = []
    
    for _, student_row in instructor_students.iterrows():
        student_name = student_row['student name']
        departure_time = student_row['departure_time']
        
        if pd.isna(departure_time):
            continue
            
        # Check if student worked with multiple instructors on this date
        student_all_sessions = df_checkin[
            (df_checkin['student name'] == student_name) & 
            (df_checkin['date'] == target_date)
        ]
        
        # Count unique instructors for this student
        unique_instructors = set()
        for _, session in student_all_sessions.iterrows():
            if pd.notna(session['instructors']):
                # Split instructors if multiple listed (e.g., "John, Jane")
                session_instructors = [inst.strip() for inst in str(session['instructors']).split(',')]
                unique_instructors.update(session_instructors)
        
        # Only count this student if:
        # 1. They left BEFORE instructor clocked out
        # 2. They worked with ONLY this instructor (no handoffs)
        worked_with_multiple = len(unique_instructors) > 1
        left_before_clockout = clock_out_time is None or departure_time < clock_out_time
        
        if left_before_clockout and not worked_with_multiple:
            valid_students_data.append(departure_time)
    
    if len(valid_students_data) == 0:
        return clock_out_time, None, None
    
    last_student_departure = max(valid_students_data)
    
    # Calculate cleanup time (should be positive and reasonable for normal cleanup)
    cleanup_time_minutes = None
    if clock_out_time and last_student_departure:
        # Ensure both times are on the same day
        if clock_out_time.date() == last_student_departure.date():
            cleanup_time_minutes = (clock_out_time - last_student_departure).total_seconds() / 60
            
            # Validate cleanup time is reasonable (between 0 and 120 minutes)
            if cleanup_time_minutes < 0 or cleanup_time_minutes > 120:
                cleanup_time_minutes = None  # Invalid data
        else:
            # Cross-day calculation - invalid
            cleanup_time_minutes = None
    
    return clock_out_time, last_student_departure, cleanup_time_minutes

# Style function for highlighting based on assessment
def highlight_low_performers(val, df):
    if pd.isna(val) or not isinstance(val, str):
        return ''
    # Find the row for the student name in the DataFrame
    matching_row = df[df['student name'] == val]
    if not matching_row.empty:
        pages_completed = matching_row['pages completed'].iloc[0] if 'pages completed' in matching_row.columns else float('inf')
        assessment = matching_row['had_assessment'].iloc[0] if 'had_assessment' in matching_row.columns else ''
        
        # Highlight red if: less than 5 pages AND assessment is EMPTY (no assessment work done)
        is_low_pages = pages_completed < 5
        no_assessment = pd.isna(assessment) or assessment == ''
        
        return 'color: red' if (is_low_pages and no_assessment) else 'color: black'
    return 'color: black'  # Default to black if no match

st.set_page_config(page_title="Student Learning Center Dashboard", layout="wide")
st.title("Student Learning Center Dashboard")
st.markdown("""
Welcome to your daily insights dashboard! Upload the check-in data (Excel) and scheduled appointments (CSV) to view clear, readable summaries and insightful charts on attendance, student, and instructor performance.

**🆕 NEW:** Upload employee timesheet data to see instructor cleanup time analysis - how long it takes instructors to clean up after their last student leaves!

Times are formatted nicely (e.g., 4:00 PM), and we've focused on key details without unnecessary info.
""")

excel_file = st.file_uploader("📋 Upload Check-in Data (Excel) - **Required**", type=['xlsx', 'xls'])
csv_file = st.file_uploader("📅 Upload Scheduled Appointments (CSV) - *Optional*", type='csv')
timesheet_file = st.file_uploader("⏰ Upload Employee Timesheet (Excel) - *Optional*", type=['xlsx', 'xls'])

if excel_file is not None:
    try:
        df_checkin = pd.read_excel(excel_file)
        
        # Load scheduled appointments if provided
        df_scheduled = None
        if csv_file is not None:
            df_scheduled = pd.read_csv(csv_file)
        
        # Process timesheet data if provided
        df_timesheet = None
        if timesheet_file is not None:
            df_timesheet = pd.read_excel(timesheet_file)
            df_timesheet.columns = df_timesheet.columns.str.strip().str.lower()
            
            # Clean up timesheet data - remove summary rows and NaN employee names
            df_timesheet = df_timesheet[df_timesheet['employee name'].notna()]
            df_timesheet = df_timesheet[~df_timesheet['employee name'].str.contains('Total|Grand', na=False)]
            
            # Rename columns to match our expected format
            df_timesheet = df_timesheet.rename(columns={
                'employee name': 'instructor name',
                'time out': 'clock out'
            })
            
            # Convert timesheet date and times
            if 'date' in df_timesheet.columns:
                df_timesheet['date'] = pd.to_datetime(df_timesheet['date'], errors='coerce').dt.date
                
            # Show debug info about processed timesheet
            if not df_timesheet.empty:
                st.sidebar.success(f"✅ Timesheet loaded: {len(df_timesheet)} instructor records")
                st.sidebar.write("**Instructors in timesheet:**", df_timesheet['instructor name'].unique().tolist())
            
    except Exception as e:
        st.error(f"Error reading files: {e}")
        st.stop()

    # Preprocess check-in data
    df_checkin.columns = df_checkin.columns.str.strip().str.lower()
    embedded_cols = ['session', 'general information', 'student materials', 'digital reward system', 'schoolwork']
    for col in embedded_cols:
        if col in df_checkin.columns:
            parsed_df = df_checkin[col].apply(parse_embedded_data).apply(pd.Series)
            df_checkin = pd.concat([df_checkin.drop(col, axis=1), parsed_df], axis=1)

    if 'assessment' in df_checkin.columns:
        # Set had_assessment to the assessment value if not empty/NA, otherwise empty string
        df_checkin['had_assessment'] = df_checkin['assessment'].apply(lambda x: x if pd.notna(x) and x != '' else '')

    if 'pages completed' in df_checkin.columns:
        df_checkin['pages completed'] = pd.to_numeric(df_checkin['pages completed'], errors='coerce')
        df_checkin = df_checkin.dropna(subset=['pages completed'])  # Drop rows with null pages

    df_checkin['date'] = pd.to_datetime(df_checkin['date'], errors='coerce').dt.date
    
    # Add date range filtering for multi-period analysis
    st.sidebar.header("📅 Date Range Filter")
    unique_dates = sorted(df_checkin['date'].dropna().unique())
    
    if len(unique_dates) > 1:
        # Multi-period data detected
        st.sidebar.success(f"📊 Multi-period data detected: {len(unique_dates)} days")
        st.sidebar.write(f"**Date Range:** {min(unique_dates)} to {max(unique_dates)}")
        
        # Date range selector
        col1, col2 = st.sidebar.columns(2)
        with col1:
            start_date = st.date_input("Start Date", value=min(unique_dates), min_value=min(unique_dates), max_value=max(unique_dates))
        with col2:
            end_date = st.date_input("End Date", value=max(unique_dates), min_value=min(unique_dates), max_value=max(unique_dates))
        
        # Filter data by selected date range
        df_checkin = df_checkin[(df_checkin['date'] >= start_date) & (df_checkin['date'] <= end_date)]
        
        if df_scheduled is not None:
            # Only process if scheduled_time column exists
            if 'scheduled_time' in df_scheduled.columns:
                df_scheduled['date'] = pd.to_datetime(df_scheduled['scheduled_time'].str.split(' ', n=3).str[:-1].str.join(' '), errors='coerce').dt.date
                df_scheduled = df_scheduled[(df_scheduled['date'] >= start_date) & (df_scheduled['date'] <= end_date)]
            
        if df_timesheet is not None and 'date' in df_timesheet.columns:
            df_timesheet = df_timesheet[(df_timesheet['date'] >= start_date) & (df_timesheet['date'] <= end_date)]
            
        st.sidebar.write(f"**Filtered to:** {len(df_checkin)} check-in records")
    else:
        # Single day data
        st.sidebar.info(f"📋 Single day data: {unique_dates[0] if unique_dates else 'No valid dates'}")

    # Create full datetime for actual check-in time with flexible parsing
    if 'session start' in df_checkin.columns:
        df_checkin['actual_time'] = pd.to_datetime(df_checkin['date'].astype(str) + ' ' + df_checkin['session start'], errors='coerce')

    if 'session start' in df_checkin.columns and 'session end' in df_checkin.columns:
        df_checkin['session_duration'] = df_checkin.apply(calculate_session_duration, axis=1)

    if 'instructors' in df_checkin.columns:
        df_checkin['instructors_list'] = df_checkin['instructors'].str.split(', ')
        
        # Show name matching debug info if timesheet is available
        if df_timesheet is not None and not df_timesheet.empty:
            checkin_instructors = df_checkin['instructors'].dropna().unique()
            st.sidebar.write("**Instructors in check-in data:**", checkin_instructors.tolist())
            
            # Show which names will match
            st.sidebar.write("**Name Matching Results:**")
            for checkin_name in checkin_instructors:
                matches = []
                for timesheet_name in df_timesheet['instructor name'].unique():
                    if names_match(checkin_name, timesheet_name):
                        matches.append(timesheet_name)
                
                if matches:
                    st.sidebar.write(f"✅ '{checkin_name}' → {matches}")
                else:
                    st.sidebar.write(f"❌ '{checkin_name}' → No match found")

    if 'internal notes' in df_checkin.columns:
        df_checkin['internal notes'] = df_checkin['internal notes'].astype(str)

    # Preprocess scheduled data if available
    df_merged = None
    if df_scheduled is not None:
        df_scheduled.columns = df_scheduled.columns.str.strip().str.lower()
        # Handle different possible column names for appointments
        column_mapping = {
            'studentname': 'student name',
            'appointmentdate': 'scheduled_time',
            'appointment date': 'scheduled_time',  # This is the actual column name!
            'student name': 'student name',  # already correct
            'date': 'scheduled_time',
            'time': 'scheduled_time'
        }
        
        # Apply available mappings
        for old_col, new_col in column_mapping.items():
            if old_col in df_scheduled.columns:
                df_scheduled.rename(columns={old_col: new_col}, inplace=True)
        
        # Only process if we have the required scheduled_time column
        if 'scheduled_time' in df_scheduled.columns:
            if 'date' not in df_scheduled.columns:
                df_scheduled['date'] = pd.to_datetime(df_scheduled['scheduled_time'].str.split(' ', n=3).str[:-1].str.join(' '), errors='coerce').dt.date
            df_scheduled['scheduled_time'] = pd.to_datetime(df_scheduled['scheduled_time'], errors='coerce')
        else:
            st.warning("⚠️ Scheduled appointments file missing required 'appointmentdate' column")
            df_scheduled = None

        # Filter for confirmed appointments only if we still have scheduled data
        if df_scheduled is not None and 'status' in df_scheduled.columns:
            # Handle different status formats
            confirmed_statuses = ['Appointment Confirmed', 'APPOINTMENT_CONFIRMED', 'Confirmed', 'CONFIRMED']
            df_scheduled = df_scheduled[df_scheduled['status'].isin(confirmed_statuses)]

        # Merge on student name and date if we still have valid scheduled data
        if df_scheduled is not None and not df_scheduled.empty:
            try:
                df_merged = pd.merge(df_scheduled, df_checkin, on=['student name', 'date'], how='outer', indicator=True)
                df_merged['Attended'] = df_merged['_merge'] == 'both'
                df_merged['Walk-In'] = df_merged['_merge'] == 'right_only'
                df_merged['No-Show'] = df_merged['_merge'] == 'left_only'
            except Exception as e:
                st.error(f"Error merging data: {e}")
                # Fall back to check-in only mode
                df_scheduled = None
        else:
            # No valid scheduled data - set to None for downstream logic
            df_scheduled = None
    
    # Create basic merged dataset if no scheduled data
    if df_scheduled is None:
        df_merged = df_checkin.copy()
        df_merged['Attended'] = True  # All check-in records are attended
        df_merged['Walk-In'] = True   # All are walk-ins since no scheduled data
        df_merged['No-Show'] = False  # No no-shows since we don't have scheduled data

    # Calculate time difference
    if 'actual_time' in df_merged.columns and 'scheduled_time' in df_merged.columns:
        df_merged['time_difference'] = df_merged.apply(lambda row: calculate_time_difference(row['scheduled_time'], row['actual_time']) if pd.notna(row['scheduled_time']) and pd.notna(row['actual_time']) else None, axis=1)
        df_merged['Early/Late Status'] = df_merged['time_difference'].apply(lambda x: 'On Time' if pd.isna(x) else ('Late' if x > 15 else ('Early' if x < -15 else 'On Time')))

    # Format times for display
    if 'scheduled_time' in df_merged.columns:
        df_merged['Scheduled Time'] = df_merged['scheduled_time'].dt.strftime('%I:%M %p')
    if 'actual_time' in df_merged.columns:
        df_merged['Check-In Time'] = df_merged['actual_time'].dt.strftime('%I:%M %p')
    if 'time_difference' in df_merged.columns:
        df_merged['Time Difference (Minutes)'] = df_merged['time_difference'].apply(lambda x: f"{x:.0f}" if pd.notnull(x) else 'N/A')

    # Identify low performers (less than 5 pages, no assessment)
    low_performers = []
    if 'had_assessment' in df_checkin.columns and 'pages completed' in df_checkin.columns:
        low_performers = df_checkin[(df_checkin['pages completed'] < 5) & (df_checkin['had_assessment'] == '')]['student name'].unique()

    # Determine which insights are available
    has_scheduled_data = df_scheduled is not None
    has_timesheet_data = df_timesheet is not None and not df_timesheet.empty
    is_multi_period = len(unique_dates) > 1
    
    # Dynamic tab creation based on available data
    tab_names = ["📋 Check-in Analysis", "👥 Student Performance", "👨‍🏫 Instructor Performance"]
    if has_scheduled_data:
        tab_names.insert(0, "📊 Attendance Overview")
    if is_multi_period:
        tab_names.append("📈 Time Analysis")
        tab_names.append("🚨 Repeat Offenders")
    tab_names.append("📊 Center Stats")
    
    tabs = st.tabs(tab_names)
    tab_idx = 0

    # Attendance Overview tab (only if scheduled data is available)
    if has_scheduled_data:
        with tabs[tab_idx]:
            st.subheader("📊 Attendance Overview")
            st.info("This analysis requires both check-in data and scheduled appointments.")
            
            num_came_in = len(df_merged[df_merged['Attended']])
            st.metric("Number of Students Who Came In", num_came_in)

            walk_ins = df_merged[df_merged['Walk-In']][['date', 'student name', 'Check-In Time']]
            walk_ins.columns = ['Date', 'Walk-In Students', 'Check-In Time']
            st.write("Walk-In Students")
            if len(walk_ins) > 0:
                styled_walk_ins = walk_ins.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Walk-In Students'])
                st.dataframe(styled_walk_ins, hide_index=True)
            else:
                st.write("No walk-ins today.")

            no_shows = df_merged[df_merged['No-Show']][['date', 'student name', 'Scheduled Time']]
            st.write("No-Show Students")
            if len(no_shows) > 0:
                no_shows.columns = ['Date', 'Student Name', 'Scheduled Time']
                st.dataframe(no_shows.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Student Name']), hide_index=True)
            else:
                st.write("No no-shows today.")

            st.write("Scheduled vs Check-In Times")
            if 'time_difference' in df_merged.columns:
                time_comparison = df_merged[df_merged['Attended']][['date', 'student name', 'Scheduled Time', 'Check-In Time', 'Time Difference (Minutes)', 'Early/Late Status']]
                time_comparison = time_comparison.sort_values(by='Time Difference (Minutes)', ascending=True)
                time_comparison.columns = ['Date', 'Student Name', 'Scheduled Time', 'Check-In Time', 'Time Difference (Minutes)', 'Early/Late Status']
                styled_time = time_comparison.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Student Name'])
                st.dataframe(styled_time, hide_index=True)
            else:
                st.write("Unable to calculate time differences - missing actual or scheduled times.")

            super_late_early = time_comparison[time_comparison['Early/Late Status'] != 'On Time'] if 'Early/Late Status' in time_comparison.columns else pd.DataFrame()
            st.write("Students Super Late or Super Early (15+ Minutes Off)")
            if len(super_late_early) > 0:
                styled_super = super_late_early.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Student Name'])
                st.dataframe(styled_super, hide_index=True)
            else:
                st.write("No students were super late or early today.")
        
        tab_idx += 1

    # Check-in Analysis tab (always available with just Excel file)
    with tabs[tab_idx]:
        st.subheader("📋 Check-in Analysis")
        st.success("✅ This analysis works with just the check-in data!")
        
        # Basic check-in statistics
        total_sessions = len(df_checkin)
        unique_students = df_checkin['student name'].nunique() if 'student name' in df_checkin.columns else 0
        unique_instructors = df_checkin['instructors'].nunique() if 'instructors' in df_checkin.columns else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Sessions", total_sessions)
        with col2:
            st.metric("Unique Students", unique_students)
        with col3:
            st.metric("Unique Instructors", unique_instructors)
            
        # Show date range if multi-period
        if is_multi_period:
            st.write(f"📅 **Period:** {min(df_checkin['date'])} to {max(df_checkin['date'])} ({len(unique_dates)} days)")
    
    tab_idx += 1

    # Student Performance tab
    with tabs[tab_idx]:
        st.subheader("👥 Student Performance")
        if 'pages completed' in df_checkin.columns:
            avg_page_count = df_checkin['pages completed'].mean()
            st.metric("Overall Average Pages Completed", f"{avg_page_count:.2f}")

            low_pages_students = df_checkin[df_checkin['pages completed'] < 5]
            num_low_pages = len(low_pages_students)
            percent_low_pages = (num_low_pages / len(df_checkin) * 100) if len(df_checkin) > 0 else 0
            st.metric("Percentage of Students with Less Than 5 Pages", f"{percent_low_pages:.2f}%")

            st.write("Students with Less Than 5 Pages")
            low_pages_display = low_pages_students[['student name', 'pages completed', 'had_assessment']]
            low_pages_display.columns = ['Student Name', 'Pages Completed', 'Assessment Details']
            styled_low = low_pages_display.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Student Name'])
            st.dataframe(styled_low, hide_index=True)

            st.write("All Students' Pages Completed")
            individual_pages = df_checkin[['student name', 'pages completed', 'had_assessment']]
            individual_pages.columns = ['Student Name', 'Pages Completed', 'Assessment Details']
            styled_individual = individual_pages.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Student Name'])
            st.dataframe(styled_individual, hide_index=True)
    
    tab_idx += 1

    # Instructor Performance tab
    with tabs[tab_idx]:
        st.subheader("👨‍🏫 Instructor Performance")
        if has_timesheet_data:
            st.info("📊 Enhanced with timesheet data - cleanup times available!")
        else:
            st.warning("⚠️ Upload timesheet data to see cleanup time analysis")
        if 'instructors_list' in df_checkin.columns:
            df_instr = df_checkin.explode('instructors_list')
            instructors = df_instr['instructors_list'].unique()
            st.write("Instructors Present Today")
            if 'date' in df_instr.columns:
                days_worked_df = (
                    df_instr.groupby('instructors_list')['date']
                    .nunique()
                    .reset_index()
                )
                days_worked_df.columns = ['Instructor', 'Days Worked']
                st.dataframe(days_worked_df.sort_values('Instructor'), hide_index=True)
            else:
                st.dataframe(pd.DataFrame({'Instructors': instructors}))

            instructor_stats = df_instr.groupby('instructors_list').agg(
                Students_Worked_With=('student name', 'nunique'),
                Total_Pages=('pages completed', 'sum'),
                Average_Pages=('pages completed', 'mean')
            ).reset_index()

            instructor_stats.columns = ['Instructor', 'Students Worked With', 'Total Pages', 'Average Pages']

            # Vectorized calculation for % Less Than 5 Pages
            less_than_5 = df_instr[df_instr['pages completed'] < 5].groupby('instructors_list').size()
            total_students = df_instr.groupby('instructors_list').size()
            instructor_stats['% Students < 5 Pages'] = (less_than_5 / total_students * 100).fillna(0).reindex(instructor_stats['Instructor']).values

            # Add cleanup time data if timesheet is available - FIXED for multi-day
            if df_timesheet is not None:
                cleanup_times = []
                for instructor in instructor_stats['Instructor']:
                    # Calculate average cleanup time across all days this instructor worked
                    instructor_dates = df_checkin[df_checkin['instructors'].str.contains(instructor, na=False)]['date'].unique()
                    daily_cleanup_times = []
                    
                    for date in instructor_dates:
                        _, _, cleanup_minutes = calculate_instructor_cleanup_time(instructor, df_checkin, df_timesheet, date)
                        if cleanup_minutes is not None and cleanup_minutes >= 0:  # Only positive cleanup times
                            daily_cleanup_times.append(cleanup_minutes)
                    
                    # Average cleanup time across days
                    if daily_cleanup_times:
                        avg_cleanup = sum(daily_cleanup_times) / len(daily_cleanup_times)
                        cleanup_times.append(avg_cleanup)
                    else:
                        cleanup_times.append(None)
                
                instructor_stats['Cleanup Time (min)'] = cleanup_times

            st.write("Instructor Summary")
            format_cols = ['Average Pages', '% Students < 5 Pages']
            if 'Cleanup Time (min)' in instructor_stats.columns:
                format_cols.append('Cleanup Time (min)')
                
                # Calculate and display team average cleanup time
                valid_cleanup_times = [t for t in instructor_stats['Cleanup Time (min)'] if t is not None and pd.notna(t)]
                if valid_cleanup_times:
                    avg_cleanup = sum(valid_cleanup_times) / len(valid_cleanup_times)
                    
                    # PROMINENT CLEANUP TIME ANALYSIS
                    st.error("🎯 **INSTRUCTOR CLEANUP GOAL: <20 MINUTES**")
                    
                    # Show prominent cleanup time summary
                    if is_multi_period:
                        st.success(f"🗓️ **Monthly Cleanup Analysis** - {len(unique_dates)} days of data")
                        
                        # Create detailed cleanup summary with goal tracking
                        cleanup_summary = instructor_stats[instructor_stats['Cleanup Time (min)'].notna()][['Instructor', 'Cleanup Time (min)']].copy()
                        cleanup_summary = cleanup_summary.sort_values('Cleanup Time (min)')
                        cleanup_summary['Status'] = cleanup_summary['Cleanup Time (min)'].apply(
                            lambda x: '✅ Under Goal' if x < 20 else '⚠️ Over Goal' if x < 30 else '🚨 Way Over'
                        )
                        cleanup_summary['Cleanup Time (min)'] = cleanup_summary['Cleanup Time (min)'].apply(lambda x: f"{x:.1f} min")
                        
                        col1, col2 = st.columns([2, 1])
                        with col1:
                            st.write("**📊 Instructor Cleanup Performance**")
                            st.dataframe(cleanup_summary, hide_index=True)
                        with col2:
                            col_a, col_b = st.columns(2)
                            with col_a:
                                over_goal_count = len([t for t in valid_cleanup_times if t > 20])
                                st.metric("📊 Team Average", f"{avg_cleanup:.1f} min")
                                st.metric("🚨 Over Goal", f"{over_goal_count}/{len(valid_cleanup_times)}")
                            with col_b:
                                st.metric("📈 Worst", f"{max(valid_cleanup_times):.1f} min")
                                st.metric("📉 Best", f"{min(valid_cleanup_times):.1f} min")
                        
                        # Goal achievement summary
                        under_goal = len([t for t in valid_cleanup_times if t < 20])
                        over_goal = len([t for t in valid_cleanup_times if t >= 20])
                        if over_goal > 0:
                            st.error(f"🚨 **{over_goal} out of {len(valid_cleanup_times)} instructors** are averaging over the 20-minute goal!")
                        else:
                            st.success(f"🎉 **All {under_goal} instructors** are meeting the 20-minute cleanup goal!")
                    else:
                        # Daily view - simpler metrics with goal emphasis
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            color = "normal" if avg_cleanup < 20 else "inverse"
                            st.metric("📊 Team Average", f"{avg_cleanup:.1f} min", delta=f"{avg_cleanup-20:.1f} from goal")
                        with col2:
                            st.metric("📈 Max Cleanup Time", f"{max(valid_cleanup_times):.1f} min")
                        with col3:
                            st.metric("📉 Min Cleanup Time", f"{min(valid_cleanup_times):.1f} min")
                    
            st.dataframe(instructor_stats.style.format("{:.1f}", subset=format_cols))

            for instructor in instructors:
                with st.expander(f"Details for {instructor}", expanded=False):
                    instr_students = df_instr[df_instr['instructors_list'] == instructor].copy()
                    avg_pages = instr_students['pages completed'].mean()
                    st.metric("Average Pages Completed by Students", f"{avg_pages:.2f}")

                    low_pages = instr_students[instr_students['pages completed'] < 5]
                    num_low = len(low_pages)
                    percent_low = (num_low / len(instr_students) * 100) if len(instr_students) > 0 else 0
                    st.metric("% of Students with Less Than 5 Pages", f"{percent_low:.2f}%")

                    # Calculate cleanup time if timesheet data is available - FIXED for multi-day
                    if df_timesheet is not None:
                        # Get instructor's work dates
                        instructor_dates = df_checkin[df_checkin['instructors'].str.contains(instructor, na=False)]['date'].unique()
                        
                        # Calculate cleanup stats across all days
                        daily_cleanup_times = []
                        most_recent_data = None
                        
                        for date in sorted(instructor_dates, reverse=True):  # Most recent first
                            clock_out, last_student_departure, cleanup_minutes = calculate_instructor_cleanup_time(
                                instructor, df_checkin, df_timesheet, date
                            )
                            
                            if cleanup_minutes is not None and cleanup_minutes >= 0:
                                daily_cleanup_times.append(cleanup_minutes)
                                
                            # Store most recent valid data for display
                            if most_recent_data is None and clock_out is not None:
                                most_recent_data = (clock_out, last_student_departure, cleanup_minutes)
                        
                        if most_recent_data or daily_cleanup_times:
                            col1, col2, col3 = st.columns(3)
                            
                            if most_recent_data:
                                clock_out, last_student_departure, _ = most_recent_data
                                with col1:
                                    clock_out_str = clock_out.strftime('%I:%M %p') if clock_out else 'N/A'
                                    st.metric("Recent Clock Out", clock_out_str)
                                with col2:
                                    last_departure_str = last_student_departure.strftime('%I:%M %p') if last_student_departure else 'N/A'
                                    st.metric("Recent Last Student", last_departure_str)
                            else:
                                with col1:
                                    st.metric("Recent Clock Out", "N/A")
                                with col2:
                                    st.metric("Recent Last Student", "N/A")
                            
                            with col3:
                                if daily_cleanup_times:
                                    avg_cleanup = sum(daily_cleanup_times) / len(daily_cleanup_times)
                                    if is_multi_period:
                                        st.metric("📊 Overall Avg Cleanup", f"{avg_cleanup:.1f} min", 
                                                help=f"Average across {len(daily_cleanup_times)} working days")
                                    else:
                                        st.metric("Avg Cleanup Time", f"{avg_cleanup:.1f} min")
                                else:
                                    st.metric("Avg Cleanup Time", "N/A")
                        
                        # Show additional monthly stats if available
                        if is_multi_period and daily_cleanup_times:
                            st.info(f"📈 **Monthly Cleanup Stats:** {len(daily_cleanup_times)} days worked | "
                                   f"Range: {min(daily_cleanup_times):.1f} - {max(daily_cleanup_times):.1f} min | "
                                   f"Average: {avg_cleanup:.1f} min")
                        
                        # DAILY CLEANUP BREAKDOWN - Show each day's cleanup time
                        st.markdown("#### 📅 **Daily Cleanup Time Breakdown**")
                        
                        # Get all days this instructor worked and their cleanup times
                        daily_breakdown = []
                        instructor_dates = df_checkin[df_checkin['instructors'].str.contains(instructor, na=False)]['date'].unique()
                        
                        for date in sorted(instructor_dates):
                            clock_out, last_student_departure, cleanup_minutes = calculate_instructor_cleanup_time(
                                instructor, df_checkin, df_timesheet, date
                            )
                            
                            # Format the data for display
                            breakdown_row = {
                                'Date': date.strftime('%Y-%m-%d'),
                                'Clock Out': clock_out.strftime('%I:%M %p') if clock_out else 'No Data',
                                'Last Student Left': last_student_departure.strftime('%I:%M %p') if last_student_departure else 'No Data',
                                'Cleanup Time (min)': f"{cleanup_minutes:.1f}" if cleanup_minutes is not None else 'No Data',
                                'Status': '✅ Good' if cleanup_minutes and cleanup_minutes < 20 else 
                                         '⚠️ Over Goal' if cleanup_minutes and cleanup_minutes < 30 else 
                                         '🚨 Way Over' if cleanup_minutes and cleanup_minutes >= 30 else 
                                         '❌ No Data'
                            }
                            daily_breakdown.append(breakdown_row)
                        
                        if daily_breakdown:
                            breakdown_df = pd.DataFrame(daily_breakdown)
                            st.dataframe(breakdown_df, hide_index=True)
                            
                            # Debug info for missing data
                            no_data_days = len([row for row in daily_breakdown if row['Cleanup Time (min)'] == 'No Data'])
                            if no_data_days > 0:
                                st.warning(f"⚠️ **{no_data_days} days** missing cleanup data - check timesheet coverage")
                        else:
                            st.error("❌ No working days found for this instructor")
                            
                        # TROUBLESHOOTING SECTION for missing averages
                        if not daily_cleanup_times or len(daily_cleanup_times) == 0:
                            st.markdown("#### 🔍 **Troubleshooting Missing Cleanup Data**")
                            
                            # Check name matching
                            timesheet_instructors = df_timesheet['instructor name'].unique() if df_timesheet is not None else []
                            name_matches = [name for name in timesheet_instructors if names_match(instructor, name)]
                            
                            st.write(f"**Instructor Name in Check-ins:** '{instructor}'")
                            st.write(f"**Available Timesheet Names:** {timesheet_instructors.tolist()}")
                            st.write(f"**Name Matches Found:** {name_matches}")
                            
                            # Check date coverage
                            if name_matches:
                                matched_name = name_matches[0]
                                timesheet_dates = df_timesheet[df_timesheet['instructor name'] == matched_name]['date'].unique()
                                checkin_dates = instructor_dates
                                
                                st.write(f"**Timesheet Dates for {matched_name}:** {sorted(timesheet_dates)}")
                                st.write(f"**Check-in Dates:** {sorted(checkin_dates)}")
                                
                                # Check for missing dates
                                missing_dates = set(checkin_dates) - set(timesheet_dates)
                                if missing_dates:
                                    st.error(f"**Missing timesheet data for dates:** {sorted(missing_dates)}")
                            else:
                                st.error(f"**No name match found for '{instructor}' in timesheet data**")
                                # Suggest closest matches
                                similarities = []
                                for ts_name in timesheet_instructors:
                                    # Simple similarity check
                                    if instructor.lower().split()[0] in ts_name.lower():
                                        similarities.append(ts_name)
                                if similarities:
                                    st.info(f"**Possible matches:** {similarities}")

                    # Show students sorted by departure time
                    st.write("Students Worked With (Sorted by Departure Time)")
                    students_with_departure = instr_students.copy()
                    if 'session end' in students_with_departure.columns and 'date' in students_with_departure.columns:
                        students_with_departure['departure_time'] = students_with_departure.apply(calculate_student_departure_time, axis=1)
                        students_with_departure = students_with_departure.sort_values('departure_time')
                        
                        display_cols = ['date', 'student name', 'session start', 'session end', 'pages completed']
                        if 'departure_time' in students_with_departure.columns:
                            students_with_departure['departure_formatted'] = students_with_departure['departure_time'].dt.strftime('%I:%M %p')
                            display_cols.append('departure_formatted')
                        
                        student_display = students_with_departure[display_cols].copy()
                        if 'departure_formatted' in student_display.columns:
                            student_display.columns = ['Date', 'Student Name', 'Session Start', 'Session End', 'Pages Completed', 'Departure Time']
                        else:
                            student_display.columns = ['Date', 'Student Name', 'Session Start', 'Session End', 'Pages Completed']
                        
                        styled_students = student_display.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Student Name'])
                        st.dataframe(styled_students, hide_index=True)
                    else:
                        st.write("Session time data not available for sorting.")

                    st.write("Students with Less Than 5 Pages")
                    low_pages_display = low_pages[['student name', 'pages completed', 'had_assessment']]
                    low_pages_display.columns = ['Student Name', 'Pages Completed', 'Assessment Details']
                    styled_low_instr = low_pages_display.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Student Name'])
                    st.dataframe(styled_low_instr, hide_index=True)
    
    tab_idx += 1

    # Time Analysis tab (only for multi-period data)
    if is_multi_period:
        with tabs[tab_idx]:
            st.subheader("📈 Time Analysis")
            st.success(f"🗓️ Analyzing {len(unique_dates)} days of data")
            
            # Daily trends
            agg_dict = {
                'student name': 'count',
                'pages completed': ['mean', 'sum']
            }
            
            # Only include instructors if the column exists
            if 'instructors' in df_checkin.columns:
                agg_dict['instructors'] = 'nunique'
            
            daily_stats = df_checkin.groupby('date').agg(agg_dict).round(2)
            
            # Set column names based on what columns we have
            if 'instructors' in df_checkin.columns:
                daily_stats.columns = ['Total Sessions', 'Avg Pages/Session', 'Total Pages', 'Unique Instructors']
            else:
                daily_stats.columns = ['Total Sessions', 'Avg Pages/Session', 'Total Pages']
            daily_stats = daily_stats.reset_index()
            
            st.write("📊 Daily Trends")
            st.dataframe(daily_stats, hide_index=True)
            
            # Time-based charts
            col1, col2 = st.columns(2)
            
            with col1:
                fig_sessions = px.line(daily_stats, x='date', y='Total Sessions', 
                                     title='📅 Daily Sessions Over Time',
                                     markers=True)
                st.plotly_chart(fig_sessions, use_container_width=True)
                
            with col2:
                fig_avg_pages = px.line(daily_stats, x='date', y='Avg Pages/Session',
                                      title='📖 Average Pages per Session Over Time',
                                      markers=True)
                st.plotly_chart(fig_avg_pages, use_container_width=True)
            
            # Period summary
            period_days = (max(df_checkin['date']) - min(df_checkin['date'])).days + 1
            total_sessions = len(df_checkin)
            total_students = df_checkin['student name'].nunique()
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("📅 Period Length", f"{period_days} days")
            with col2:
                st.metric("📊 Total Sessions", total_sessions)
            with col3:
                st.metric("👥 Unique Students", total_students)
            with col4:
                st.metric("📈 Avg Sessions/Day", f"{total_sessions/period_days:.1f}")
        
        tab_idx += 1

    # Repeat Offenders Analysis tab (only for multi-period data)
    if is_multi_period:
        with tabs[tab_idx]:
            st.subheader("🚨 Repeat Offenders Analysis")
            st.error(f"⚠️ **Problem Students & Patterns** - Analysis across {len(unique_dates)} days")
            
            # Instructor Cleanup Issues - PRIORITY #1
            st.markdown("### 🔥 **INSTRUCTOR CLEANUP ANALYSIS** - Goal: <20 minutes")
            if df_timesheet is not None:
                cleanup_analysis = []
                
                for instructor in df_checkin['instructors'].str.split(', ').explode().unique():
                    if pd.isna(instructor):
                        continue
                        
                    instructor_dates = df_checkin[df_checkin['instructors'].str.contains(instructor, na=False)]['date'].unique()
                    daily_cleanup_times = []
                    
                    for date in instructor_dates:
                        _, _, cleanup_minutes = calculate_instructor_cleanup_time(instructor, df_checkin, df_timesheet, date)
                        if cleanup_minutes is not None and 0 <= cleanup_minutes <= 120:
                            daily_cleanup_times.append(cleanup_minutes)
                    
                    if daily_cleanup_times:
                        avg_cleanup = sum(daily_cleanup_times) / len(daily_cleanup_times)
                        days_over_20 = len([t for t in daily_cleanup_times if t > 20])
                        worst_day = max(daily_cleanup_times)
                        
                        cleanup_analysis.append({
                            'Instructor': instructor,
                            'Avg Cleanup (min)': round(avg_cleanup, 1),
                            'Days Worked': len(daily_cleanup_times),
                            'Days Over 20min': days_over_20,
                            '% Over Goal': round((days_over_20 / len(daily_cleanup_times)) * 100, 1),
                            'Worst Day (min)': round(worst_day, 1)
                        })
                
                if cleanup_analysis:
                    cleanup_df = pd.DataFrame(cleanup_analysis)
                    cleanup_df = cleanup_df.sort_values('Avg Cleanup (min)', ascending=False)
                    
                    # Highlight problematic instructors
                    def highlight_cleanup_issues(row):
                        if row['Avg Cleanup (min)'] > 20:
                            return ['background-color: #ffebee'] * len(row)  # Light red
                        elif row['% Over Goal'] > 50:
                            return ['background-color: #fff3e0'] * len(row)  # Light orange
                        else:
                            return ['background-color: #e8f5e8'] * len(row)  # Light green
                    
                    styled_cleanup = cleanup_df.style.apply(highlight_cleanup_issues, axis=1)
                    st.dataframe(styled_cleanup, hide_index=True)
                    
                    worst_instructors = cleanup_df[cleanup_df['Avg Cleanup (min)'] > 20]
                    if not worst_instructors.empty:
                        st.error(f"🚨 **{len(worst_instructors)} instructors** averaging >20 min cleanup!")
                        for _, row in worst_instructors.iterrows():
                            st.write(f"- **{row['Instructor']}**: {row['Avg Cleanup (min)']} min avg, {row['% Over Goal']}% of days over goal")
                    
                    # DEBUG: Show instructors with no cleanup data
                    all_instructors = df_checkin['instructors'].str.split(', ').explode().unique()
                    instructors_with_data = [row['Instructor'] for row in cleanup_analysis]
                    instructors_without_data = [instr for instr in all_instructors if pd.notna(instr) and instr not in instructors_with_data]
                    
                    if instructors_without_data:
                        st.warning(f"⚠️ **{len(instructors_without_data)} instructors** have NO cleanup data:")
                        for instructor in instructors_without_data:
                            st.write(f"- **{instructor}**: Check timesheet coverage or name matching")
                else:
                    st.error("❌ No cleanup analysis data available - check timesheet upload and date coverage")
            
            # Student Repeat Offenders
            st.markdown("### 📚 **STUDENT REPEAT OFFENDERS**")
            
            # Low Performance Repeat Offenders
            if 'pages completed' in df_checkin.columns and 'had_assessment' in df_checkin.columns:
                student_performance = df_checkin.groupby('student name').agg({
                    'pages completed': ['count', 'mean'],
                    'had_assessment': lambda x: (x == '').sum()  # Count empty assessments
                }).round(2)
                
                student_performance.columns = ['Total Sessions', 'Avg Pages', 'Sessions No Assessment']
                student_performance = student_performance.reset_index()
                student_performance['% Low Performance'] = ((df_checkin.groupby('student name').apply(
                    lambda x: ((x['pages completed'] < 5) & (x['had_assessment'] == '')).sum()
                ) / student_performance['Total Sessions']) * 100).round(1)
                
                # Find repeat low performers
                repeat_low_performers = student_performance[
                    (student_performance['% Low Performance'] > 30) & 
                    (student_performance['Total Sessions'] >= 3)
                ].sort_values('% Low Performance', ascending=False)
                
                if not repeat_low_performers.empty:
                    st.warning(f"📉 **{len(repeat_low_performers)} students** with consistent low performance:")
                    st.dataframe(repeat_low_performers, hide_index=True)
            
            # Attendance Pattern Offenders (if scheduled data available)
            if has_scheduled_data:
                st.markdown("### 📅 **ATTENDANCE PATTERN OFFENDERS**")
                
                # No-show repeat offenders
                no_show_analysis = df_merged[df_merged['No-Show']]['student name'].value_counts()
                frequent_no_shows = no_show_analysis[no_show_analysis >= 2]
                
                if not frequent_no_shows.empty:
                    st.error(f"🚫 **{len(frequent_no_shows)} students** with multiple no-shows:")
                    for student, count in frequent_no_shows.items():
                        st.write(f"- **{student}**: {count} no-shows")
                
                # Walk-in repeat offenders
                walk_in_analysis = df_merged[df_merged['Walk-In']]['student name'].value_counts()
                frequent_walk_ins = walk_in_analysis[walk_in_analysis >= 3]
                
                if not frequent_walk_ins.empty:
                    st.warning(f"🚶 **{len(frequent_walk_ins)} students** frequently walk-in:")
                    for student, count in frequent_walk_ins.items():
                        st.write(f"- **{student}**: {count} walk-ins")
                
                # Late/Early repeat offenders
                if 'time_difference' in df_merged.columns:
                    time_patterns = df_merged[df_merged['time_difference'].notna()].groupby('student name')['time_difference'].agg(['count', 'mean'])
                    time_patterns = time_patterns[time_patterns['count'] >= 3]  # At least 3 appointments
                    
                    chronically_late = time_patterns[time_patterns['mean'] > 15]
                    chronically_early = time_patterns[time_patterns['mean'] < -15]
                    
                    if not chronically_late.empty:
                        st.error(f"⏰ **{len(chronically_late)} students** chronically late:")
                        for student, data in chronically_late.iterrows():
                            st.write(f"- **{student}**: Avg {data['mean']:.1f} min late")
                    
                    if not chronically_early.empty:
                        st.info(f"⏰ **{len(chronically_early)} students** chronically early:")
                        for student, data in chronically_early.iterrows():
                            st.write(f"- **{student}**: Avg {abs(data['mean']):.1f} min early")
        
        tab_idx += 1

    # Center Stats tab
    with tabs[tab_idx]:
        st.subheader("📊 Center Stats Overview")
        
        # Show what data is being analyzed
        data_sources = []
        if has_scheduled_data:
            data_sources.append("✅ Scheduled Appointments")
        if has_timesheet_data:
            data_sources.append("✅ Employee Timesheets")
        data_sources.append("✅ Check-in Data")
        
        st.info(f"📋 **Data Sources:** {' | '.join(data_sources)}")
        
        # Attendance Trend Bar Chart (only if scheduled data available)
        if has_scheduled_data:
            attendance_data = {
                'Category': ['Attended', 'Walk-Ins', 'No-Shows'],
                'Count': [len(df_merged[df_merged['Attended']]), len(df_merged[df_merged['Walk-In']]), len(df_merged[df_merged['No-Show']])]
            }
            fig_attendance = px.bar(attendance_data, x='Category', y='Count', title='Daily Attendance Summary',
                                   color='Category', color_discrete_map={'Attended': '#2ECC71', 'Walk-Ins': '#3498DB', 'No-Shows': '#E74C3C'},
                                   text='Count', height=400)
            fig_attendance.update_traces(textposition='auto')
            st.plotly_chart(fig_attendance, use_container_width=True)

        # Student Performance Bar Chart with specified buckets
        if 'pages completed' in df_checkin.columns:
            bins = [0, 1, 3, 5, 7, 9, 11, float('inf')]
            labels = ['0-1 Pages', '2-3 Pages', '4-5 Pages', '6-7 Pages', '8-9 Pages', '10-11 Pages', '12+ Pages']
            df_checkin['Page Bucket'] = pd.cut(df_checkin['pages completed'], bins=bins, labels=labels, include_lowest=True, right=False)
            performance_dist = df_checkin['Page Bucket'].value_counts().reindex(labels, fill_value=0).reset_index()
            performance_dist.columns = ['Page Range', 'Count']
            fig_performance_bar = px.bar(performance_dist, x='Page Range', y='Count', title='Student Performance Distribution',
                                         color='Page Range', color_discrete_sequence=px.colors.qualitative.Pastel, height=400)
            fig_performance_bar.update_traces(textposition='auto')
            st.plotly_chart(fig_performance_bar, use_container_width=True)

        # Instructor Performance Comparison Bar Chart
        if 'instructors_list' in df_checkin.columns:
            df_instr = df_checkin.explode('instructors_list')
            instructor_stats = df_instr.groupby('instructors_list').agg(
                Average_Pages=('pages completed', 'mean')
            ).reset_index()
            fig_instructor_bar = px.bar(instructor_stats.sort_values('Average_Pages', ascending=False),
                                      x='Average_Pages', y='instructors_list', title='Instructor Performance Comparison',
                                      color='Average_Pages', color_continuous_scale='Viridis', height=400)
            st.plotly_chart(fig_instructor_bar, use_container_width=True)

        # Time Difference Distribution Bar Chart
        if 'time_difference' in df_merged.columns:
            time_diff_data = df_merged[df_merged['Attended']].copy()
            # Filter out None values before cutting
            time_diff_data = time_diff_data[time_diff_data['time_difference'].notna()]
            if not time_diff_data.empty:
                time_diff_data['Time Diff Bin'] = pd.cut(time_diff_data['time_difference'], bins=[-float('inf'), -15, -5, 5, 15, float('inf')],
                                                        labels=['>15 min Early', '5-15 min Early', 'On Time', '5-15 min Late', '>15 min Late'])
                time_diff_dist = time_diff_data['Time Diff Bin'].value_counts().reset_index()
                time_diff_dist.columns = ['Time Difference', 'Count']
                fig_time_diff = px.bar(time_diff_dist, x='Time Difference', y='Count', title='Time Difference Distribution',
                                      color='Time Difference', color_discrete_map={
                                          '>15 min Early': '#2ECC71', '5-15 min Early': '#3498DB', 'On Time': '#F1C40F',
                                          '5-15 min Late': '#E67E22', '>15 min Late': '#E74C3C'}, height=400)
                fig_time_diff.update_traces(textposition='auto')
                st.plotly_chart(fig_time_diff, use_container_width=True)
            else:
                st.write("No valid time difference data to display.")

else:
    st.info("📋 **Please upload the check-in Excel file to get started!**")
    st.markdown("""
    ### 🚀 What you can do:
    
    **📋 With just the Check-in Excel file:**
    - ✅ Student performance analysis  
    - ✅ Instructor statistics
    - ✅ Pages completed insights
    - ✅ Multi-period analysis (if your file contains multiple dates)
    
    **📊 Add Scheduled Appointments CSV for:**
    - ➕ Attendance vs. scheduled analysis
    - ➕ Walk-in vs. scheduled student tracking
    - ➕ No-show identification
    - ➕ Time difference analysis (early/late arrivals)
    
    **⏰ Add Employee Timesheet Excel for:**
    - ➕ Instructor cleanup time analysis
    - ➕ Time between last student departure and instructor clock-out
    - ➕ Team average cleanup metrics
    
    **📈 Multi-period Analysis:**
    - Upload files with multiple dates to see trends over time!
    - Automatic date range filtering
    - Daily averages and time-based charts
    """)
