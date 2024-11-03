import random  
len = int(input("Enter the desired password len: "))
def generate_password(len):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()" 
    password = ""  
    for i in range(len):
        password += random.choice(characters)  
    return password
print("Generated Password:", generate_password(len))
