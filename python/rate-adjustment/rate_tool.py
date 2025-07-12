import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize rates in session state if not present
if 'rates' not in st.session_state:
    st.session_state.rates = {
        '2x': {
            'Elementary': {7: 439, 12: 419, 18: 399, 24: 379},
            'Middle':     {7: 459, 12: 439, 18: 419, 24: 399},
            'High':       {7: 519, 12: 489, 18: 469, 24: 449},
        },
        '1x': {
            'Elementary': {7: 269, 12: 249, 18: 239, 24: 229},
            'Middle':     {7: 279, 12: 259, 18: 249, 24: 239},
            'High':       {7: 299, 12: 279, 18: 269, 24: 259},
        }
    }

# --- Utility Functions ---
def get_base_rate(grade, plan_type, term):
    return st.session_state.rates[plan_type][grade][term]

def determine_nearest_plan(months):
    return min([7, 12, 18, 24], key=lambda x: abs(x - months))

def apply_discount(rate, value, is_percent):
    return rate * (1 - value / 100) if is_percent else rate - value

def calculate_months(start_date, end_date):
    return max(1, round((end_date - start_date).days / 30))

def generate_email(student, parent_name, months, adjusted_term,
                   base_original, base_adjusted, original_rate, adjusted_rate,
                   total_paid, adjusted_total, diff):

    direction = "Credit" if diff < 0 else "Amount Owed"
    diff = abs(diff)
    discount_label = f"{student['discount_value']:.2f}%" if student['discount_is_percent'] else f"${student['discount_value']:.2f}"
    subject_line = f"Membership Rate Update for {student['name']}"

    return f"""
<html>
<body style="font-family: 'Poppins', sans-serif; line-height: 1.6; color: #1d1d1f;">
<h4 style="color: #ed1c24; font-weight: 600; margin-bottom: 10px;">Subject: {subject_line}</h4>
<p>Dear {parent_name},</p>
<br>

<p>Thank you for being such a valued part of our Mathnasium family! We’re committed to supporting {student['name']}'s learning journey and ensuring fairness for all our families. I’m reaching out to share a clear and friendly update about {student['name']}'s membership rate, adjusted to reflect their enrollment timeline, as part of our commitment to equitable pricing.</p>

<hr style="border: 0; height: 1px; background: #dee2e6; margin: 20px 0;">

<h4 style="color: #1d1d1f;">Program Details</h4>
<ul style="list-style-type: disc; padding-left: 20px;">
    <li><b>Student</b>: {student['name']}</li>
    <li><b>Original Program</b>: {student['membership_term']}-month | {student['grade'].capitalize()} | {student['plan_type']}/week</li>
    <li><b>Start Date</b>: {student['start_date'].strftime('%B %d, %Y')}</li>
    <li><b>End Date</b>: {student['end_date'].strftime('%B %d, %Y')}</li>
    <li><b>Months Attended</b>: Approximately {months}</li>
</ul>

<hr style="border: 0; height: 1px; background: #dee2e6; margin: 20px 0;">

<h4 style="color: #1d1d1f;">Membership Rate Adjustment</h4>
<p>Based on {student['name']}'s {months} month(s) of attendance, we’ve adjusted their membership to align with our <b>{adjusted_term}-month program</b>, which best matches their time with us. We’ve fully applied your original discount of <b>{discount_label}</b> to ensure you receive the same great value.</p>

<hr style="border: 0; height: 1px; background: #dee2e6; margin: 20px 0;">

<h4 style="color: #1d1d1f;">Financial Summary</h4>

<p><b>Original Membership</b></p>
<ul style="list-style-type: disc; padding-left: 20px;">
    <li>Monthly Rate: <b>${base_original:.2f} → ${original_rate:.2f} (with discount)</b></li>
    <li>Total Paid: <b>${total_paid:.2f}</b></li>
</ul>

<p><b>Adjusted Membership</b></p>
<ul style="list-style-type: disc; padding-left: 20px;">
    <li>Monthly Rate: <b>${base_adjusted:.2f} → ${adjusted_rate:.2f} (with discount)</b></li>
    <li>Adjusted Total: <b>${adjusted_total:.2f}</b></li>
</ul>

<p><b>{direction}</b>: <b>${diff:.2f}</b></p>

<hr style="border: 0; height: 1px; background: #dee2e6; margin: 20px 0;">

<h4 style="color: #1d1d1f;">What’s Next?</h4>
<p>This rate adjustment reflects our standard process to align the monthly rate with the actual time {student['name']} has been enrolled, ensuring fairness for every family. We’re here to make this as smooth as possible for you, so if you have any questions or need further clarification, please don’t hesitate to reach out—I’d be delighted to assist!</p>

<p>We’re so grateful to have {student['name']} and your family with us at Mathnasium! Thank you for trusting us with their math journey!</p>

<br>
<p>Warmest regards,<br>

</body>
</html>
"""

# --- Mathnasium-Inspired CSS: Bold, Energetic, Clean ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    .stApp {
        background-color: #ffffff;
        color: #1d1d1f;
        font-family: 'Poppins', sans-serif;
        max-width: 900px;
        margin: 0 auto;
        padding: 40px 20px;
    }
    .stHeader {
        font-size: 2.5em;
        font-weight: 600;
        color: #ed1c24;
        text-align: center;
        margin-bottom: 40px;
    }
    .instructions {
        font-size: 1.1em;
        color: #6e6e73;
        text-align: center;
        margin-bottom: 40px;
    }
    .student-section {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 18px;
        margin-bottom: 30px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .student-title {
        font-size: 1.8em;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 25px;
        text-align: center;
    }
    .stButton > button {
        background-color: #ed1c24;
        color: white;
        border-radius: 12px;
        padding: 12px;
        border: none;
        font-size: 1em;
        font-weight: 600;
        transition: background-color 0.3s ease, transform 0.1s ease;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #d4181f;
        transform: translateY(-1px);
    }
    .stTextInput > div > div > input, .stSelectbox > div > div > div > button, .stDateInput > div > div > input, .stNumberInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #d2d2d7;
        padding: 10px;
        font-size: 1em;
        transition: border-color 0.3s ease;
    }
    .stTextInput > div > div > input:focus, .stSelectbox > div > div > div > button:focus, .stDateInput > div > div > input:focus, .stNumberInput > div > div > input:focus {
        border-color: #ed1c24;
        box-shadow: 0 0 0 2px rgba(237, 28, 36, 0.2);
    }
    .stRadio > div {
        display: flex;
        justify-content: flex-start;
    }
    .stRadio > div > label {
        margin-right: 20px;
    }
    .email-output {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 18px;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .stCaption {
        color: #6e6e73;
        font-size: 0.9em;
        text-align: center;
        margin-top: 10px;
    }
    /* Add some white space and visual hierarchy */
    [data-testid="column"] {
        padding: 0 10px;
    }
    /* Tooltips for help */
    .stTooltip {
        background-color: #ffd700;
        color: #1d1d1f;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 0.9em;
    }
    .price-banner {
        background-color: rgba(255, 215, 0, 0.1);
        border: 1px solid rgba(255, 215, 0, 0.3);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 30px;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
        position: relative;
        overflow: hidden;
    }
    .price-banner::before {
        content: '';
        position: absolute;
        top: -5px; right: -5px; bottom: -5px; left: -5px;
        background: linear-gradient(45deg, #ffd700, #ffea00, #ffd700);
        z-index: -1;
        filter: blur(10px);
        opacity: 0.4;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Streamlit UI ---
st.set_page_config(page_title="Mathnasium Rate Adjustment Tool", page_icon="📬", layout="wide")

st.markdown('<div class="stHeader">Mathnasium Rate Adjustment Tool</div>', unsafe_allow_html=True)

st.markdown('<div class="instructions">Welcome to Mathnasium! Easily calculate rate adjustments for your student\'s membership. Enter details below and generate a professional email with one click.</div>', unsafe_allow_html=True)

# Clickable dropdown for price adjustment at the top with subtle glowing yellow banner
with st.expander("Adjust Prices (for different states/centers)"):
    st.markdown('<div class="price-banner">', unsafe_allow_html=True)
    st.header("Customize Rates")
    st.markdown("Edit the rates for your center/state below. Changes will apply immediately.")

    # Create square matrix tables for 1x and 2x
    terms = [7, 12, 18, 24]
    grades = ['Elementary', 'Middle', 'High']

    st.subheader("1x per Week Rates")
    data_1x = {grade: [st.session_state.rates['1x'][grade][term] for term in terms] for grade in grades}
    df_1x = pd.DataFrame(data_1x, index=terms).T
    edited_1x = st.data_editor(df_1x, use_container_width=True)

    st.subheader("2x per Week Rates")
    data_2x = {grade: [st.session_state.rates['2x'][grade][term] for term in terms] for grade in grades}
    df_2x = pd.DataFrame(data_2x, index=terms).T
    edited_2x = st.data_editor(df_2x, use_container_width=True)

    # Button to update rates
    if st.button("Update Rates"):
        # Update 1x rates
        for grade in grades:
            for j, term in enumerate(terms):
                st.session_state.rates['1x'][grade][term] = edited_1x.iloc[grades.index(grade), j]

        # Update 2x rates
        for grade in grades:
            for j, term in enumerate(terms):
                st.session_state.rates['2x'][grade][term] = edited_2x.iloc[grades.index(grade), j]

        st.success("Rates updated successfully!")
    st.markdown('</div>', unsafe_allow_html=True)

parent_name = st.text_input("Parent's Name", placeholder="Enter parent's name", help="The name of the parent or guardian to address in the email.")

num_students = st.number_input("Number of Students", min_value=1, max_value=5, value=1, step=1, help="Select how many students to process (up to 5 for simplicity).")

for i in range(num_students):
    with st.container():
        st.markdown('<div class="student-section">', unsafe_allow_html=True)
        st.markdown(f'<div class="student-title">Student {i+1}</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1,1], gap="medium")

        with col1:
            student_name = st.text_input("Name", placeholder="Enter student's name", key=f"name_{i}", help="Full name of the student.")
            grade = st.selectbox("Grade Level", options=['Elementary', 'Middle', 'High'], key=f"grade_{i}", help="Select the grade level.")
            plan = st.selectbox("Program Type", options=['1x', '2x'], key=f"plan_{i}", help="Sessions per week.")

        with col2:
            term = st.selectbox("Original Term (months)", options=[7, 12, 18, 24], key=f"term_{i}", help="Original membership duration.")
            start = st.date_input("Start Date", key=f"start_{i}", help="When the membership started.")
            end = st.date_input("End Date", value=datetime.today(), key=f"end_{i}", help="When the membership ends.")

        col3, col4 = st.columns([1,1], gap="medium")

        with col3:
            discount_type = st.radio("Discount Type", options=['%', '$'], horizontal=True, key=f"discount_type_{i}", help="Percentage or fixed dollar amount.")

        with col4:
            discount_value = st.number_input("Discount Amount", min_value=0.0, step=0.01, key=f"discount_value_{i}", help="Value of the discount.")

        if st.button("Generate Email", key=f"button_{i}"):
            student = {
                "name": student_name,
                "grade": grade,
                "plan_type": plan,
                "membership_term": term,
                "start_date": start,
                "end_date": end,
                "discount_is_percent": discount_type == '%',
                "discount_value": discount_value
            }

            months = calculate_months(start, end)
            adjusted_term = determine_nearest_plan(months)

            base_original = get_base_rate(grade, plan, term)
            base_adjusted = get_base_rate(grade, plan, adjusted_term)

            original_rate = apply_discount(base_original, discount_value, student["discount_is_percent"])
            adjusted_rate = apply_discount(base_adjusted, discount_value, student["discount_is_percent"])

            total_paid = original_rate * months
            adjusted_total = adjusted_rate * months
            diff = adjusted_total - total_paid

            email = generate_email(student, parent_name, months, adjusted_term,
                                   base_original, base_adjusted, original_rate, adjusted_rate,
                                   total_paid, adjusted_total, diff)

            st.markdown('<div class="email-output">', unsafe_allow_html=True)
            st.subheader(f"Email for {student_name or f'Student {i+1}'}")
            st.markdown(email, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.caption("Copy and paste this into your email app.")

        st.markdown('</div>', unsafe_allow_html=True)

# Footer with Mathnasium branding
st.markdown("""
<div style="text-align: center; margin-top: 50px; color: #6e6e73; font-size: 0.9em;">
    Powered by Mathnasium | Making Math Make Sense
</div>
""", unsafe_allow_html=True)
