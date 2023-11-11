import string
import random

def generate_pass(len):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(len))
    return password

pass_len = int(input("Enter the desired length of the password: "))
generate_pass = generate_pass(pass_len)
print("Your generated password is:",generate_pass)