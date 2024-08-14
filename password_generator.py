import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    if length < 1:
        return "Error: Password length must be at least 1 character."

    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        if length < 1:
            print("The password length must be at least 1 character.")
            return
        
    except ValueError:
        print("Please enter a valid number.")
        return
    
    password = generate_password(length)
    
    print(f"Generated password: {password}")
    print("Make sure to save this password in a secure place!")

if __name__ == "__main__":
    main()
