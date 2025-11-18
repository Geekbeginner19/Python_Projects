# 🔥 Beginner-Friendly Python Project of the Day
# Project: Simple Password Strength Checker

# Perfect for your level — no OOP, real-life use case, uses functions, strings, conditions, loops.

# 🎯 Goal
# Create a program that checks how strong a password is based on rules.

# 🧩 Requirements
# ✔️ 1. Ask the user to enter a password.
# ✔️ 2. Check the following rules:

# Length at least 8 characters
# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one digit
# Contains at least one special character
# (!@#$%^&*()-_=+[]{};:,.<>?)

# ✔️ 3. Output strength levels:
# Very Weak → fails 3 or more rules
# Weak → fails 2 rules
# Medium → fails 1 rule
# Strong → passes all rules

# ✔️ 4. After showing strength, ask:
# Do you want to check another password? (y/n)
# Loop until user chooses n.


def pass_strength(password):
    failures = 0
    specials = "!@#$%^&*()-_=+[]{};:,.<>?"

    if len(password) < 8:
        failures += 1
    
    if not any(ch.isupper() for ch in password):
        failures += 1

    if not any(ch.islower() for ch in password):
        failures += 1

    if not any(ch.isdigit() for ch in password):
        failures += 1

    if not any(ch in specials for ch in password):
        failures += 1

    return failures


def get_strength_label(failures):
    if failures == 0:
        return "Strong"
    elif failures == 1:
        return "Medium"
    elif failures == 2:
        return "Weak"
    else:
        return "Very Weak"

while True:
    password = input("Please enter a password: ")
    failures = pass_strength(password)
    print(get_strength_label(failures))
    password = input("Do you want to check another password? (y/n) ").lower()
    if (password.lower() == "n"):
        break
