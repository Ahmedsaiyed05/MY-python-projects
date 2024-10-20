while True:
    print('''List of Indian states for weather: 
    1. Gujarat
    2. Mumbai
    3. Delhi 
    4. Goa
    5. Kerala 
    6. Madhya Pradesh''')

    try:
        select = int(input("Select the Indian state for weather info (1-6): "))

        if select == 1:
            print("Gujarat has weather 29 degrees.")

        elif select == 2:
            print("***Mumbai has weather 32 degrees***.")

        elif select == 3:
            print("***Delhi has weather 22 degrees***.")

        elif select == 4:
            print("***Goa has weather 32 degrees***.")

        elif select == 5:
            print("***Kerala has weather 32 degrees***.")

        elif select == 6:
            print("***Madhya Pradesh has weather 24 degrees***.")
        
        else:
            print("Invalid selection. Please select a number from 1 to 6.")

    except ValueError: 
        print("Please select a valid number (no strings).")
