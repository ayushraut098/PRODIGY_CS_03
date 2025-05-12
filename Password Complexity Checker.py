import re

def assess_password_strength(password):
    min_length = 8
    max_length = 20

    if len(password) < min_length:
        length_feedback = f"Password is too short. It should be at least {min_length} characters long."
    elif len(password) > max_length:
        length_feedback = f"Password is too long. It should not exceed {max_length} characters."
    else:
        length_feedback = "Password length is good."

    if not re.search(r'[A-Z]', password):
        case_feedback = "Password should contain at least one uppercase letter."
    else:
        case_feedback = "Password contains uppercase letters."

    if not re.search(r'[a-z]', password):
        case_feedback += " Password should contain at least one lowercase letter."
    else:
        case_feedback += " Password contains lowercase letters."

    if not re.search(r'[0-9]', password):
        number_feedback = "Password should contain at least one number."
    else:
        number_feedback = "Password contains numbers."

    if not re.search(r'[^A-Za-z0-9]', password):
        special_char_feedback = "Password should contain at least one special character (e.g., @, #, $, etc.)."
    else:
        special_char_feedback = "Password contains special characters."

    if len(password) >= min_length and len(password) <= max_length and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[^A-Za-z0-9]', password):
        strength = "Strong"
    elif len(password) >= min_length and (re.search(r'[A-Z]', password) or re.search(r'[a-z]', password)) and (re.search(r'[0-9]', password) or re.search(r'[^A-Za-z0-9]', password)):
        strength = "Medium"
    else:
        strength = "Weak"

    return f"{length_feedback}\n{case_feedback}\n{number_feedback}\n{special_char_feedback}\nPassword Strength: {strength}"

password = input("Enter a password to assess its strength: ")
print(assess_password_strength(password))
