class calculator: 
    def add (num1 , num2):
        return num1 + num2 
    def sub (num1 , num2):
        return num1 - num2 
    def div (num1 , num2):
        return num1 / num2 
    def multi (num1 , num2):
        return num1 * num2 
    
print('''*1.add\n
*2.sub\n
*3.div\n
*4.multi\n''')
try:
    select = int(input("what you want to calculate :"))
    
    if select == str:
       raise ValueError("you cant enter a sting ")
    if select < 1 or select > 4: 
        raise ValueError("please enter a valid number not blank space")
    number1 = int(input("number 1 : "))
    number2 = int(input("number 2 : "))
    if select == 1:
     print(calculator.add(number1 , number2))
    elif select == 2:
     print(calculator.sub(number1 , number2))
    elif select == 3:
     if number1 == 0 or number2 == 0:
        raise ZeroDivisionError("can't divide by zero") 
     print(calculator.div(number1 , number2))
     if number1 == 0 or number2 == 0:
        raise ZeroDivisionError("can't divide by zero") 
    elif select == 4:
     print(calculator.multi(number1 , number2))  
except ValueError as v : 
   print("error: 404 value not found :( ")
except ZeroDivisionError as z :
   print("error:cant be divide or multiply by zero")
except ValueError as s : 
   print("this is str")