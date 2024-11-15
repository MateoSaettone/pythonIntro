############################################
#                                          #
#     HOSPITAL PATIENT DATA STATISTICS     #
#                                          #
#          MATEO SAETTONE ASCENZO          #
#               U56111212                  #
#                                          #
############################################

# read patient data from file
with open('Week13Assignment.txt', 'r') as file:
    lines = file.readlines()

# initialize lists and counters
ages = []
male_count = 0
female_count = 0
blood_pressures = []
temperatures = []

# parse each line, skip the header
for line in lines[1:]:
    # split line into fields
    fields = line.strip().split(',')
    # get data
    name = fields[0].strip()
    age = int(fields[1].strip())
    gender = fields[2].strip()
    bp = fields[3].strip()
    temp = float(fields[4].strip())

    # collect data
    ages.append(age)
    temperatures.append(temp)
    blood_pressures.append(bp)

    # count genders
    if gender.lower() == 'male':
        male_count += 1
    elif gender.lower() == 'female':
        female_count += 1

# calculate averages
average_age = sum(ages) / len(ages)
average_temp = sum(temperatures) / len(temperatures)

# convert bp readings to tuples for comparison
bp_tuples = []

for bp_str in blood_pressures:
    systolic_diastolic = bp_str.split('/')
    systolic = int(systolic_diastolic[0])
    diastolic = int(systolic_diastolic[1])
    bp_tuples.append((systolic, diastolic))

# find highest and lowest bp
highest_bp = max(bp_tuples)
lowest_bp = min(bp_tuples)

# format bp readings
highest_bp_str = f"{highest_bp[0]}/{highest_bp[1]}"
lowest_bp_str = f"{lowest_bp[0]}/{lowest_bp[1]}"

# print statistics
print("Patient Data Statistics:")
print(f"Average Age: {average_age:.2f}")
print(f"Males: {male_count}")
print(f"Females: {female_count}")
print(f"Highest Blood Pressure: {highest_bp_str}")
print(f"Lowest Blood Pressure: {lowest_bp_str}")
print(f"Average Temperature: {average_temp:.2f}")
