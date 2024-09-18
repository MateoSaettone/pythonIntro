############################################
#                                          #
#          Temperature Calculator          # 
#                                          #
#          Mateo Saettone Ascenzo          #
#                U56111212                 #
#                                          #
############################################

# Function to determine whether the temperature is high or not
def isTemperatureHigh(temp):
    if temp >= 99.5:
        print("The patient has a high temperature.")
    elif temp < 99.5:
        print("The patient's temperature is normal.")

# Main function to handle input and do input verification using a try except block
def main():
    try:
        temp = float(input("Enter the patient's temperature (in degrees Fahrenheit): "))
        float(temp)
    except ValueError:
        print("Error: Please enter a valid temperature (numeric value).")
        return

    isTemperatureHigh(temp)

# Run the program
main()

