# Write a program to test password strength based on length, complexity, 
# characters, and patterns. Use it to evaluate common passwords.


'''should have atleast 8 character, 12 is a safer choice'''
'''uppercase, lowercase,special character, Numbers'''

import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters recommended).")

    # Character Variety
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Common Weak Patterns
    common_patterns = [
        r"1234",
        r"password",
        r"qwerty",
        r"abc123",
        r"(.)\1{2,}"  # repeated characters (aaa, 111)
    ]

    for pattern in common_patterns:
        if re.search(pattern, password.lower()):
            score -= 1
            feedback.append("Avoid common patterns or repeated characters.")
            break

    # Common Password Check
    common_passwords = ["password", "123456", "12345678", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("This is a commonly used password!")

    # Strength Rating
    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength, feedback = check_password_strength(pwd)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for item in feedback:
            print("-", item)
