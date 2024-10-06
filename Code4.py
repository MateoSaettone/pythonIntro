############################################
#                                          #
#         Convert body temperatures        # 
#                                          #
#          Mateo Saettone Ascenzo          #
#                U56111212                 #
#                                          #
############################################

# Function 1: Celsius to Fahrenheit Conversion
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function 2: Fahrenheit to Celsius Conversion
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Main function to handle user input, choice, and conversion
def main():
    print("Choose the conversion direction:")
    print("C - Celsius to Fahrenheit")
    print("F - Fahrenheit to Celsius")

    choice = input("Enter your choice (C/F): ").lower()  # Convert choice to lowercase to handle both 'C' and 'c', 'F' and 'f'

    if choice == 'c':
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.1f} degrees Celsius is equal to {fahrenheit:.1f} degrees Fahrenheit.")
    
    elif choice == 'f':
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.1f} degrees Fahrenheit is equal to {celsius:.1f} degrees Celsius.")
    
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

main()