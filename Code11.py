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
maleCount = 0
femaleCount = 0
bloodPressures = []
temperatures = []

# parse each line (skip header)
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
    bloodPressures.append(bp)

    # count genders
    if gender.lower() == 'male':
        maleCount += 1
    elif gender.lower() == 'female':
        femaleCount += 1

# calculate averages
averageAge = sum(ages) / len(ages)
averageTemp = sum(temperatures) / len(temperatures)

# convert bp readings to tuples for comparison
bpTuples = []
for bpStr in bloodPressures:
    systolicDiastolic = bpStr.split('/')
    systolic = int(systolicDiastolic[0])
    diastolic = int(systolicDiastolic[1])
    bpTuples.append((systolic, diastolic))

# find highest and lowest bp
highestBp = max(bpTuples)
lowestBp = min(bpTuples)

# format bp readings
highestBpStr = f"{highestBp[0]}/{highestBp[1]}"
lowestBpStr = f"{lowestBp[0]}/{lowestBp[1]}"

# print statistics
print("Patient Data Statistics: \n")
print(f"AverageAge: {averageAge:.2f}")
print(f"MalePatients: {maleCount}")
print(f"FemalePatients: {femaleCount}")
print(f"HighestBloodPressure: {highestBpStr}")
print(f"LowestBloodPressure: {lowestBpStr}")
print(f"AverageTemperature: {averageTemp:.2f}")
