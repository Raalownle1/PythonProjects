import random
#Create the password length of 32 characters
def generate_password(length=32):
    # Generate a random password of the specified length
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{}[]<>,.?/;':"
    password = "".join(random.choice(characters) for _ in range(length))

    # Ensure that the password contains an uppercase, lowercase, special character and number
    while not (any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in "!@#$%^&*()-_=+{}[]<>,.?/;':" for c in password)):
        password = "".join(random.choice(characters) for _ in range(length))

    return password

# Generate a password
password = generate_password()

# Print the password
print(password)
