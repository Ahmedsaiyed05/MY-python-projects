def dollar(amount):
    return amount * 83.35

def pound(amount):
    return amount * 104.91

def aed(amount):
    return amount * 22.70


print('''1. dollar : 83
2. pound : 104.91
3. aed  : 22.70
          ''')

try:
    userChose = int(input("Please enter the number corresponding to the currency you want to convert to Indian currency: "))
    print(f"You chose option {userChose}")
    # if userChose <=3 :
    #     raise ValueError("plz enter under the above mantioned")

    amount = int(input("Amount you would like to exchange: "))

    if userChose == 1:
        result = dollar(amount)
        print(f"{amount} dollars in Indian currency is: {result}")

    elif userChose == 2:
        result = pound(amount)
        print(f"{amount} pounds in Indian currency is: {result}")

    elif userChose == 3:
        result = aed(amount)
        print(f"{amount} aed in Indian currency is: {result}")

    else:
        if userChose <=4 :
            print("4 number is not there")

except ValueError:
    print("Invalid input. Please enter a valid number.")