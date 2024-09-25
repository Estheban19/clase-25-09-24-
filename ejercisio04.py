import re

validate_password = lambda p: bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$', p))

password = input("Enter your password: ")
print("Valid password" if validate_password(password) else "Invalid password")