# Calculator for pressure using force and area

print("Hello there user, this is a pressure calculator")

while True:
    options = input("What do you want to find today? (pressure, force, area): ").lower()

    if options == 'pressure':
        print("Okay enter values of force and Area")
        force = float(input("Enter force in Newtons : "))
        area = float(input("Enter area in square meters: ")) 
        answer = force / area
        print(f'The pressure is {answer} Pa')
    elif options == 'force':
        print("Okay, Enter the values of pressure and Area")
        pressure = float(input("Enter pressure in Pa: "))
        area = float(input("Enter area in sq. m.: "))
        answer = pressure * area
        print(f"The force is {answer} N.")
    elif options == 'area':
        print("Okay Enter the values of pressure and force")
        force = float(input("Enter force in N: "))
        pressure = float(input("Enter pressure in Pa: "))
        answer = force / pressure
        print(f"The area is {answer} sq. m.")
    else:
        print("Please enter valid input")

    