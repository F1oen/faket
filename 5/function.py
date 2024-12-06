def Celsfahre(celsius):
    return(celsius * 9/5) + 32
def Fahrecels(fahrenheit):
    return(fahrenheit - 32 ) * 5/9
choice = input("Convert from C or F:").upper()
temperature = float(input("Enter the  temperature: "))
if choice == 'C':
    print(f"Temperature in Fahrenheit: {Celsfahre(temperature)}")
elif choice == 'F':
    print(f"Temperature in Celsius: {Fahrecels(temperature)}")
else:
    print("Invalid choice")