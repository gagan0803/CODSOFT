import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

try:
    length = int(input("Enter the length of the password: "))
    
    if length <= 0:
        print("Please enter valid password length.")
    else:
        password = generate_password(length)
        print(f"Generated Password is: {password}")

except ValueError:
    print("Please enter a valid integer for the password length.")
