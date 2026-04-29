import re

def check_password(password):
    strength = "Weak"

    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password) and
        re.search(r"[!@#$%^&*]", password)):
        strength = "Strong"
    elif len(password) >= 6:
        strength = "Medium"

    return strength

password = input("Enter password: ")
print("Password Strength:", check_password(password))
