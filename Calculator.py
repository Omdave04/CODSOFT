print("Simple Calculator Design!!!")
print("1. For Addition use '+' ")
print("2. For Subtraction use '-' ")
print("3. For Multiplication use '*' ")
print("4. For Division use '/' ")
print("5. For Modulus use '%' ")

def T_Calculator():
    num_1 = float(input("Enter the first number :- "))
    num_2 = float(input("Enter the second number :- "))

    C_Operation = input("Enter the operation (+,-,*,/,%) :- ")

    if C_Operation == '+':
        result = num_1 + num_2
        print(f"The result of {num_1} + {num_2} is {result}")
    elif C_Operation == '-':
        result = num_1 - num_2
        print(f"The result of {num_1} - {num_2} is {result}")
    elif C_Operation == '*':
        result = num_1 * num_2
        print(f"The result of {num_1} * {num_2} is {result}")
    elif C_Operation == '/':
        if num_2 != 0:
            result = num_1 / num_2
            print(f"The result of {num_1} / {num_2} is {result}")
        else:
            print("Warning: Division by zero is not allowed!!!")
    elif C_Operation == '%':
        result = num_1 % num_2
        print(f"The result of {num_1} % {num_2} is {result}")
    else:
        print("Invalid operation choice.")
    return True

while True:
    if not T_Calculator():
        break
    continue_choice = input("Do you want to perform another calculation ?\n yes to continue, no to stop :- ")
    if continue_choice == 'no':
        break
