############################################
#                                          #
#      Patient Health Data Analysis        #
#            with OOP Approach             #
#                                          #
#          Mateo Saettone Ascenzo          #
#               U56111212                  #
#                                          #
############################################

# patient class to store health data
class Patient:
    # initialize patient info
    def __init__(self, name, age, gender, blood_pressure, temperature):
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_pressure = blood_pressure
        self.temperature = temperature

    # show patient details
    def display_patient_info(self):
        print(f"\nPatient Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Blood Pressure: {self.blood_pressure}")
        print(f"Temperature: {self.temperature}")

    # check if patient has high blood pressure
    def is_hypertensive(self):
        systolic, diastolic = self.blood_pressure
        return systolic >= 140 or diastolic >= 90

    # check if patient has a fever
    def is_feverish(self):
        return self.temperature >= 37.5

# main function
def main():
    # create two patient examples
    patient1 = Patient("Benjamin Jacob", 40, "Male", (140, 85), 36.8)
    patient2 = Patient("Mateo Saettone", 22, "Male", (120, 80), 37.6)

    # show info and check health status for patient1
    patient1.display_patient_info()
    print("Hypertensive:", patient1.is_hypertensive())
    print("Feverish:", patient1.is_feverish())

    # show info and check health status for patient2
    patient2.display_patient_info()
    print("Hypertensive:", patient2.is_hypertensive())
    print("Feverish:", patient2.is_feverish())

# run the main function
main()
