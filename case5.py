password = input("Enter password to test: ")

has_upper = False
has_lower = False
has_digit = False

if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

is_valid = (len(password) >= 8) and has_upper and has_lower and has_digit

print("--- Password Validation Report ---")
print("Length >= 8 characters:", len(password) >= 8)
print("Contains Uppercase Letter:", has_upper)
print("Contains Lowercase Letter:", has_lower)
print("Contains Digit:", has_digit)

if is_valid:
    print("Final Status: STRONG (Password meets all criteria)")
else:
    print("Final Status: WEAK (Password failed security policy)")