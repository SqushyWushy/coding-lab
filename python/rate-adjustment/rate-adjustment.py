import datetime

def get_valid_input(prompt, valid_options):
    while True:
        val = input(prompt).strip().lower()
        if val in valid_options:
            return val
        print(f"Please enter one of the following: {', '.join(valid_options)}.")

def get_valid_int(prompt, valid_values):
    while True:
        try:
            val = int(input(prompt))
            if val in valid_values:
                return val
        except ValueError:
            pass
        print(f"Please enter a valid number: {valid_values}")

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_valid_date(prompt):
    while True:
        try:
            val = input(prompt)
            return datetime.datetime.today() if val.lower() == 'today' else datetime.datetime.strptime(val, '%m/%d/%Y')
        except ValueError:
            print("Use MM/DD/YYYY or 'today'.")

def prompt_student_info():
    student = {}
    student['name'] = input("Student name: ")
    student['grade'] = get_valid_input("Grade level (Elementary/Middle/High): ", ['elementary', 'middle', 'high'])
    plan = get_valid_input("Program type (1 or 2 sessions per week): ", ['1', '2'])
    student['plan_type'] = '1x' if plan == '1' else '2x'
    student['membership_term'] = get_valid_int("Original membership (7, 12, or 18 months): ", [7, 12, 18])
    student['start_date'] = get_valid_date("Start date (MM/DD/YYYY): ")
    student['end_date'] = get_valid_date("End date (MM/DD/YYYY or today): ")
    discount_type = get_valid_input("What type of discount is this? Enter '%' for percentage or '$' for flat dollar amount: ", ['%', '$'])
    student['discount_is_percent'] = discount_type == '%'
    student['discount_value'] = get_valid_float("Discount amount (e.g. 25 for 25% or 30 for $30): ")
    return student

def get_base_rate(grade, plan_type, term):
    rates = {
        '2x': {
            'elementary': {7: 439, 12: 419, 18: 399, 24: 379},
            'middle':     {7: 459, 12: 439, 18: 419, 24: 399},
            'high':       {7: 519, 12: 489, 18: 469, 24: 449},
        },
        '1x': {
            'elementary': {7: 269, 12: 249, 18: 239, 24: 229},
            'middle':     {7: 279, 12: 259, 18: 249, 24: 239},
            'high':       {7: 299, 12: 279, 18: 269, 24: 259},
        }
    }
    return rates[plan_type][grade][term]

def determine_nearest_plan(months_attended):
    if months_attended <= 7:
        return 7
    elif months_attended <= 14:
        return 12
    else:
        return 18

def apply_discount(rate, value, is_percent):
    return rate * (1 - value / 100) if is_percent else rate - value

def calculate_months(start_date, end_date):
    delta = end_date - start_date
    return max(1, round(delta.days / 30))

def generate_email(student, base_original_rate, base_adjusted_rate, original_rate, adjusted_rate, months, adjusted_term, total_paid, adjusted_total, diff):
    direction = "credit" if diff < 0 else "balance due"
    diff = abs(diff)
    discount_label = f"{student['discount_value']:.2f}%" if student['discount_is_percent'] else f"${student['discount_value']:.2f}"

    email = f"""
Subject: Membership Rate Adjustment for {student['name']}

Hi [Parent Name],

Thank you again for being part of the Mathnasium community! I wanted to provide a full breakdown of the membership rate adjustment for {student['name']}, based on their updated enrollment timeline:

- **Original Program**: {student['membership_term']}-month, {student['grade'].capitalize()}, {student['plan_type']}/week
- **Start Date**: {student['start_date'].strftime('%B %d, %Y')}
- **End Date**: {student['end_date'].strftime('%B %d, %Y')}
- **Months Attended**: ~ {months}

Because {student['name']} attended for approximately {months} month(s), we’ve adjusted their rate to reflect the **{adjusted_term}-month program**, which is the nearest match. We've also kept the **same discount** you've had from the beginning to ensure fairness.

**Original Monthly Rate**
- Standard Rate: ${base_original_rate:.2f}
- Discount: {discount_label}
- Monthly Payment After Discount: ${original_rate:.2f}

**Adjusted Monthly Rate**
- Standard Rate: ${base_adjusted_rate:.2f}
- Discount: {discount_label}
- Monthly Payment After Discount: ${adjusted_rate:.2f}

**Total Comparison**
- Total Paid: ${total_paid:.2f}
- Adjusted Total: ${adjusted_total:.2f}
- {direction.title()}: ${diff:.2f}

As part of our policy, early cancellations result in a rate adjustment to the nearest appropriate plan. The math above shows the difference based on time attended and your consistent discount.

Let us know how you'd like to move forward—we're here to help!

Warm regards,
Hector Gonzalez
Center Director
Mathnasium of Richardson West
"""
    return email

def main():
    parent_name = input("Parent name: ")
    num_students = int(input("How many students? "))
    for _ in range(num_students):
        student = prompt_student_info()
        months = calculate_months(student['start_date'], student['end_date'])
        adjusted_term = determine_nearest_plan(months)

        base_original = get_base_rate(student['grade'], student['plan_type'], student['membership_term'])
        base_adjusted = get_base_rate(student['grade'], student['plan_type'], adjusted_term)

        original_rate = apply_discount(base_original, student['discount_value'], student['discount_is_percent'])
        adjusted_rate = apply_discount(base_adjusted, student['discount_value'], student['discount_is_percent'])

        total_paid = original_rate * months
        adjusted_total = adjusted_rate * months
        diff = adjusted_total - total_paid

        email = generate_email(student, base_original, base_adjusted, original_rate, adjusted_rate, months, adjusted_term, total_paid, adjusted_total, diff)
        email = email.replace('[Parent Name]', parent_name)
        print("\n--- EMAIL OUTPUT ---")
        print(email)

if __name__ == "__main__":
    main()
