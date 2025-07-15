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

# Style function for highlighting based on assessment
def highlight_low_performers(val, df):
    if pd.isna(val) or not isinstance(val, str):
        return ''
    # Find the row for the student name in the DataFrame
    matching_row = df[df['student name'] == val]
    if not matching_row.empty:
        assessment = matching_row['had_assessment'].iloc[0]
        return 'color: red' if assessment != '' else 'color: black'
    return 'color: black'  # Default to black if no match

st.set_page_config(page_title="Student Learning Center Dashboard", layout="wide")
st.title("Student Learning Center Dashboard")
st.markdown("""
Welcome to your daily insights dashboard! Upload the check-in data (Excel) and scheduled appointments (CSV) to view clear, readable summaries and insightful charts on attendance, student, and instructor performance.
Times are formatted nicely (e.g., 4:00 PM), and we've focused on key details without unnecessary info.
""")

excel_file = st.file_uploader("Upload Check-in Data (Excel)", type=['xlsx', 'xls'])
csv_file = st.file_uploader("Upload Scheduled Appointments (CSV)", type='csv')

if excel_file is not None and csv_file is not None:
    try:
        df_checkin = pd.read_excel(excel_file)
        df_scheduled = pd.read_csv(csv_file)
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

    # Create full datetime for actual check-in time with flexible parsing
    if 'session start' in df_checkin.columns:
        df_checkin['actual_time'] = pd.to_datetime(df_checkin['date'].astype(str) + ' ' + df_checkin['session start'], errors='coerce')

    if 'session start' in df_checkin.columns and 'session end' in df_checkin.columns:
        df_checkin['session_duration'] = df_checkin.apply(calculate_session_duration, axis=1)

    if 'instructors' in df_checkin.columns:
        df_checkin['instructors_list'] = df_checkin['instructors'].str.split(', ')

    if 'internal notes' in df_checkin.columns:
        df_checkin['internal notes'] = df_checkin['internal notes'].astype(str)

    # Preprocess scheduled data
    df_scheduled.columns = df_scheduled.columns.str.strip().str.lower()
    df_scheduled.rename(columns={'studentname': 'student name', 'appointmentdate': 'scheduled_time'}, inplace=True)
    df_scheduled['date'] = pd.to_datetime(df_scheduled['scheduled_time'].str.split(' ', n=3).str[:-1].str.join(' '), errors='coerce').dt.date
    df_scheduled['scheduled_time'] = pd.to_datetime(df_scheduled['scheduled_time'], errors='coerce')

    df_scheduled = df_scheduled[df_scheduled['status'] == 'Appointment Confirmed']

    # Merge on student name and date
    try:
        df_merged = pd.merge(df_scheduled, df_checkin, on=['student name', 'date'], how='outer', indicator=True)
        df_merged['Attended'] = df_merged['_merge'] == 'both'
        df_merged['Walk-In'] = df_merged['_merge'] == 'right_only'
        df_merged['No-Show'] = df_merged['_merge'] == 'left_only'
    except Exception as e:
        st.error(f"Error merging data: {e}")
        st.stop()

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

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Attendance Overview", "Student Performance", "Instructor Performance", "Center Stats Overview"])

    with tab1:
        st.subheader("Attendance Overview")
        num_came_in = len(df_merged[df_merged['Attended']])
        st.metric("Number of Students Who Came In", num_came_in)

        walk_ins = df_merged[df_merged['Walk-In']][['student name', 'Check-In Time']]
        walk_ins.columns = ['Walk-In Students', 'Check-In Time']
        st.write("Walk-In Students")
        if len(walk_ins) > 0:
            styled_walk_ins = walk_ins.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Walk-In Students'])
            st.dataframe(styled_walk_ins, hide_index=True)
        else:
            st.write("No walk-ins today.")

        no_shows = df_merged[df_merged['No-Show']][['student name', 'Scheduled Time']]
        st.write("No-Show Students")
        if len(no_shows) > 0:
            st.dataframe(no_shows.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['student name']), hide_index=True)
        else:
            st.write("No no-shows today.")

        st.write("Scheduled vs Check-In Times")
        if 'time_difference' in df_merged.columns:
            time_comparison = df_merged[df_merged['Attended']][['student name', 'Scheduled Time', 'Check-In Time', 'Time Difference (Minutes)', 'Early/Late Status']]
            time_comparison = time_comparison.sort_values(by='Time Difference (Minutes)', ascending=True)
            styled_time = time_comparison.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['student name'])
            st.dataframe(styled_time, hide_index=True)
        else:
            st.write("Unable to calculate time differences - missing actual or scheduled times.")

        super_late_early = time_comparison[time_comparison['Early/Late Status'] != 'On Time'] if 'Early/Late Status' in time_comparison.columns else pd.DataFrame()
        st.write("Students Super Late or Super Early (15+ Minutes Off)")
        if len(super_late_early) > 0:
            styled_super = super_late_early.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['student name'])
            st.dataframe(styled_super, hide_index=True)
        else:
            st.write("No students were super late or early today.")

    with tab2:
        st.subheader("Student Performance")
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

    with tab3:
        st.subheader("Instructor Performance")
        if 'instructors_list' in df_checkin.columns:
            df_instr = df_checkin.explode('instructors_list')
            instructors = df_instr['instructors_list'].unique()
            st.write("Instructors Present Today")
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

            st.write("Instructor Summary")
            st.dataframe(instructor_stats.style.format("{:.2f}", subset=['Average Pages', '% Students < 5 Pages']))

            for instructor in instructors:
                with st.expander(f"Details for {instructor}", expanded=False):
                    instr_students = df_instr[df_instr['instructors_list'] == instructor].copy()
                    avg_pages = instr_students['pages completed'].mean()
                    st.metric("Average Pages Completed by Students", f"{avg_pages:.2f}")

                    low_pages = instr_students[instr_students['pages completed'] < 5]
                    num_low = len(low_pages)
                    percent_low = (num_low / len(instr_students) * 100) if len(instr_students) > 0 else 0
                    st.metric("% of Students with Less Than 5 Pages", f"{percent_low:.2f}%")

                    st.write("Students with Less Than 5 Pages")
                    low_pages_display = low_pages[['student name', 'pages completed', 'had_assessment']]
                    low_pages_display.columns = ['Student Name', 'Pages Completed', 'Assessment Details']
                    styled_low_instr = low_pages_display.style.apply(lambda x: [highlight_low_performers(val, df_checkin) for val in x], axis=1, subset=['Student Name'])
                    st.dataframe(styled_low_instr, hide_index=True)

    with tab4:
        st.subheader("Center Stats Overview")
        # Attendance Trend Bar Chart
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
    st.info("Please upload both the check-in Excel and scheduled appointments CSV to view insights.")
