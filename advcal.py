def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2 if num2 != 0 else "Error: Division by zero"

def multi(num1, num2):
    return num1 * num2

print("Please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Divide\n" \
      "4. Multiply\n")

select = input("Select the above 1, 2, 3, 4: ")

# Check if the input is empty or not a number
if select.strip() == "":
    print("Input cannot be empty.")
else:
    select = int(select)
    number1 = input('Give me number 1: ')
    number2 = input('Give me number 2: ')

    if number1.strip() == "" or number2.strip() == "":
        print("Input cannot be empty.")
    else:
        number1 = float(number1)
        number2 = float(number2)

        if select == 1:
            print(f"{number1} + {number2} = {add(number1, number2)}")
        elif select == 2:
            print(f"{number1} - {number2} = {sub(number1, number2)}")
        elif select == 3:
            result = div(number1, number2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{number1} / {number2} = {result:.2f}")
        elif select == 4:
            print(f"{number1} * {number2} = {multi(number1, number2)}")
        else:
            print('Invalid prompt')
