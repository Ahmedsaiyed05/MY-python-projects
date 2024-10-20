def add(num1, num2):
    return num1 + num2 

def sub(num1, num2):
    return num1 - num2 

def multi(num1, num2):
    return num1 * num2 

def div(num1, num2):
    return num1 / num2 

print('''1. for addition\n 
2. for subtraction \n
3. for division\n
4. for multiplication\n''')

try:
    select = int(input('Choose from above 1, 2, 3, 4: '))
    if select < 1 or select > 4:
        raise ValueError("Invalid selection. Please choose from 1 to 4.")

    number1 = int(input('Give the first number: '))
    number2 = int(input('Give the second number: '))

    if select == 1:
        print(add(number1, number2))
    elif select == 2:
        print(sub(number1, number2))
    elif select == 3:
        if number2 == 0:
            raise ValueError("Cannot divide by zero.")
        print(div(number1, number2))
    elif select == 4:
        print(multi(number1, number2))

except ValueError as ve:
    print("Error: plz enter the valid number not blank ")
except ZeroDivisionError as e:
    print("An unexpected error occurred:")
