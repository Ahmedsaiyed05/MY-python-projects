# class BMIc:
def calBMI(height ,weight):
    bmi = weight / (height ** 2)
    return bmi

heigth = float(input("height"))
weight = float(input("weight"))

calculated_bmi = calBMI(heigth , weight)
print("Your BMI is:", calculated_bmi)




    
