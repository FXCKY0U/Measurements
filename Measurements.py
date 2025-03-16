
# Give the user the options of measurements they want to enter the initial value in
while True:
    print("Welcome to the measurements converter! Please select the measurement you would like to convert to:")
    print("1. cm")
    print("2. mm")
    print("3. M")
    print("4. feet")
    print("5. inches")

    # Ask the user for which value they want to convert
    option = input("Which option would you like to enter: ")
    option = int(option)

    if option == 1:
        print("You have selected cm")
        value = input("Please enter the value in cm: ")
        value = float(value)
        print("Here is the conversions:")

        mm = value * 10
        print(f"The value in mm is: {mm:.2f}")

        M = value * 0.01
        print(f"The value in M is: {M:.2f}")

        feet = value * 0.0833333
        print(f"The value in feet is: {feet:.2f}")

        inches = value
        print(f"The value in inches is: {inches:.2f}")

    elif option == 2:
        print("You have selected mm")
        value = input("Please enter the value in mm: ")
        value = float(value)
        print("Here is the conversions:")

        cm = value / 10
        print(f"The value in cm is: {cm:.2f}")

        M = value * 0.001
        print(f"The value in M is: {M:.2f}")

        feet = value * 0.00328084
        print(f"The value in feet is: {feet:.2f}")

        inches = value * 0.0393701
        print(f"The value in inches is: {inches:.2f}")

    elif option == 3:
        print("You have selected M")
        value = input("Please enter the value in M: ")
        value = float(value)
        print("Here is the conversions:")
        
        cm = value * 100
        print(f"The value in cm is: {cm:.2f}")
        
        mm = value * 1000
        print(f"The value in mm is: {mm:.2f}")

        feet = value * 3.28084
        print(f"The value in feet is: {feet:.2f}")

        inches = value * 39.3701
        print(f"The value in inches is: {inches:.2f}")

    elif option == 4:
        print("You have selected feet")
        value = input("Please enter the value in feet: ")
        value = float(value)
        print("Here is the conversions:")

        cm = value * 30.48
        print(f"The value in cm is: {cm:.2f}")

        mm = value * 304.8
        print(f"The value in mm is: {mm:.2f}")

        M = value * 0.3048
        print(f"The value in M is: {M:.2f}")

        inches = value * 12
        print(f"The value in inches is: {inches:.2f}")

    elif option == 5:
        print("You have selected inches")
        value = input("Please enter the value in inches: ")
        value = float(value)
        print("Here is the conversions:")

        cm = value * 2.54
        print(f"The value in cm is: {cm:.2f}")

        mm = value * 25.4
        print(f"The value in mm is: {mm:.2f}")

        M = value * 0.0254
        print(f"The value in M is: {M:.2f}")

        feet = value * 0.0833333
        print(f"The value in feet is: {feet:.2f}")

    else:
        print("Invalid input. Please try again.")
        continue

    break