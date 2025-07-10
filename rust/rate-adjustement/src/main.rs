use chrono::{NaiveDate, Utc};
use std::io;

#[allow(dead_code)]
#[derive(Debug)]
struct Student {
    name: String,
    grade: String,
    plan_type: String,
    membership_term: u32,
    start_date: NaiveDate,
    end_date: NaiveDate,
    discount_is_percent: bool,
    discount_value: f64,
}

fn get_input(prompt: &str) -> String {
    use std::io::Write;
    print!("{}", prompt);
    io::stdout().flush().unwrap();
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    input.trim().to_string()
}

fn parse_date(input: &str) -> NaiveDate {
    if input.to_lowercase() == "today" {
        Utc::now().naive_utc().date()
    } else {
        NaiveDate::parse_from_str(input, "%m/%d/%Y").unwrap()
    }
}

fn calculate_months(start: NaiveDate, end: NaiveDate) -> i64 {
    let days = (end - start).num_days();
    (days as f64 / 30.0).round() as i64
}

fn determine_nearest_term(months: i64) -> u32 {
    let diffs = vec![
        (7, (months - 7).abs()),
        (12, (months - 12).abs()),
        (18, (months - 18).abs()),
    ];
    diffs.into_iter().min_by_key(|(_, diff)| *diff).unwrap().0
}

fn get_base_rate(grade: &str, plan: &str, term: u32) -> f64 {
    let rates = match plan {
        "1x" => match grade {
            "elementary" => vec![(7, 269.0), (12, 249.0), (18, 239.0)],
            "middle" => vec![(7, 279.0), (12, 259.0), (18, 249.0)],
            "high" => vec![(7, 299.0), (12, 279.0), (18, 269.0)],
            _ => vec![],
        },
        "2x" => match grade {
            "elementary" => vec![(7, 439.0), (12, 419.0), (18, 399.0)],
            "middle" => vec![(7, 459.0), (12, 439.0), (18, 419.0)],
            "high" => vec![(7, 519.0), (12, 489.0), (18, 469.0)],
            _ => vec![],
        },
        _ => vec![],
    };
    rates
        .into_iter()
        .find(|(m, _)| *m == term)
        .map(|(_, r)| r)
        .unwrap_or(0.0)
}

fn apply_discount(base: f64, value: f64, is_percent: bool) -> f64 {
    if is_percent {
        base * (1.0 - value / 100.0)
    } else {
        base - value
    }
}

fn format_email(
    name: &str,
    parent: &str,
    grade: &str,
    plan: &str,
    orig_term: u32,
    adj_term: u32,
    start: &str,
    end: &str,
    months: i64,
    base_orig: f64,
    base_adj: f64,
    discount: &str,
    orig: f64,
    adj: f64,
    paid: f64,
    adj_total: f64,
    diff: f64,
) -> String {
    let direction = if diff < 0.0 { "CREDIT" } else { "BALANCE DUE" };
    let diff = diff.abs();

    format!(
        r#"Subject: Membership Rate Adjustment for {name}

Hi {parent},

Thank you again for being part of the Mathnasium community! I wanted to provide a full breakdown of the membership rate adjustment for {name}, based on their updated enrollment timeline:

- Original Program: {orig_term}-month, {grade}, {plan}/week
- Start Date: {start}
- End Date: {end}
- Months Attended: ~{months}

Because {name} attended for approximately {months} month(s), we’ve adjusted their rate to reflect the {adj_term}-month program, which is the nearest match. We've also kept the same discount you've had from the beginning to ensure fairness.

Original Monthly Rate:
- Standard Rate: ${base_orig:.2}
- Discount: {discount}
- Monthly Payment After Discount: ${orig:.2}

Adjusted Monthly Rate:
- Standard Rate: ${base_adj:.2}
- Discount: {discount}
- Monthly Payment After Discount: ${adj:.2}

Total Comparison:
- Total Paid: ${paid:.2}
- Adjusted Total: ${adj_total:.2}
- {direction}: ${diff:.2}

Let us know how you'd like to move forward—we're here to help!

Warm regards,
Hector Gonzalez
Center Director
Mathnasium of Richardson West
"#
    )
}

fn main() {
    let parent_name = get_input("Parent name: ");
    let num_students: usize = get_input("How many students? ")
        .parse()
        .expect("Invalid number");

    for _ in 0..num_students {
        let name = get_input("Student name: ");
        let grade = get_input(&format!(
            "{}'s Grade level (elementary/middle/high): ",
            name
        ));
        let plan = get_input(&format!(
            "{}'s Program type (1 or 2 sessions per week): ",
            name
        ));
        let plan_type = if plan == "1" { "1x" } else { "2x" };
        let membership_term: u32 = get_input(&format!(
            "{}'s Original membership (7, 12, or 18 months): ",
            name
        ))
        .parse()
        .expect("Invalid membership term");
        let start_date = parse_date(&get_input(&format!("{}'s Start date (MM/DD/YYYY): ", name)));
        let end_date = parse_date(&get_input(&format!(
            "{}'s End date (MM/DD/YYYY or today): ",
            name
        )));
        let discount_type = get_input("Is the discount a % or $ amount? (%/$): ");
        let is_percent = discount_type == "%";
        let discount_value: f64 = get_input("Discount amount (e.g. 25 for 25% or 30 for $30): ")
            .parse()
            .expect("Invalid discount value");

        let months = calculate_months(start_date, end_date);
        let adjusted_term = determine_nearest_term(months);

        let base_original = get_base_rate(&grade, plan_type, membership_term);
        let base_adjusted = get_base_rate(&grade, plan_type, adjusted_term);

        let monthly_original = apply_discount(base_original, discount_value, is_percent);
        let monthly_adjusted = apply_discount(base_adjusted, discount_value, is_percent);

        let total_paid = monthly_original * months as f64;
        let adjusted_total = monthly_adjusted * months as f64;
        let diff = adjusted_total - total_paid;

        let discount_label = if is_percent {
            format!("{:.2}%", discount_value)
        } else {
            format!("${:.2}", discount_value)
        };

        let email = format_email(
            &name,
            &parent_name,
            &grade.to_uppercase(),
            plan_type,
            membership_term,
            adjusted_term,
            &start_date.format("%B %d, %Y").to_string(),
            &end_date.format("%B %d, %Y").to_string(),
            months,
            base_original,
            base_adjusted,
            &discount_label,
            monthly_original,
            monthly_adjusted,
            total_paid,
            adjusted_total,
            diff,
        );

        println!("\n--- EMAIL OUTPUT ---\n{}\n", email);
    }
}
