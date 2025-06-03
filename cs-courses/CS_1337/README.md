# TableFlip++

A command-line restaurant waitlist and check-in system written in C++.

## 🚀 Overview

**TableFlip++** simulates a real-world system where customers can check in at a restaurant using their phone number. It intelligently manages a live waitlist by identifying returning customers, estimating wait times, and generating confirmation codes. Designed with Object-Oriented Programming principles in mind, this project mirrors a real business-use case.

## 📦 Features

- 📱 **Check-in system** using customer phone numbers
- 🔁 **Returning customer detection** with auto-filled info from file
- 🧾 **File I/O** for persistent storage of customer records
- 🕒 **Waitlist manager** with real-time expected wait time estimation
- 🔐 **Random confirmation code** generation
- 💡 **Input validation** and error handling

## 🧠 Core Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Vectors and maps
- File input/output (I/O)
- Random number generation
- User input validation
- Control structures and functions

## 🔧 Technologies Used

- C++
- Standard Template Library (STL): `vector`, `map`, `fstream`, `iostream`

## 🛠️ How It Works

1. On launch, the program loads existing customer data from a file (if any).
2. New customers are prompted to enter their name and phone number.
3. Returning customers are detected using their phone number and welcomed back.
4. Each check-in generates a confirmation code and is added to the waitlist.
5. The system estimates wait time based on queue length and prints live updates.

## New User:

## Welcome to TableFlip++! 🍽️

1. Check In
2. View Waitlist
3. Exit
   > 1

Enter your phone number: 5551234567

No existing record found. Let's get you added!

Enter your full name: Sarah Lopez
Party size: 4

✅ You’re checked in, Sarah!
Confirmation Code: TF9421

Estimated wait time: 25 minutes

---

Returning to main menu...

## Returning User:

## Welcome to TableFlip++! 🍽️

1. Check In
2. View Waitlist
3. Exit
   > 1

Enter your phone number: 5551234567

Welcome back, Sarah Lopez!
Party of 4, returning guest.

✅ You’re checked in again!
Confirmation Code: TF1048

Estimated wait time: 20 minutes

---

Returning to main menu...

## View Waitlist:

## Current Waitlist:

1. Sarah Lopez — Party of 4 — 20 min
2. Alex Wang — Party of 2 — 15 min
3. Maya Patel — Party of 3 — 18 min

---

## 🗃 File Structure

```bash
📁 CS_1337/
├── computer-science-1.md       # Course notes
├── main.cpp                    # Main application logic
├── Customer.hpp / .cpp         # Customer class and behavior
├── Waitlist.hpp / .cpp         # Waitlist handling logic
├── utils.cpp                   # Utility functions (validation, formatting)
└── data/
    └── customers.txt           # Stored customer check-in data
```
