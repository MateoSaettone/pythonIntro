############################################
#                                          #
#         Epidemiological Calculator       # 
#                                          #
#          Mateo Saettone Ascenzo          #
#                U56111212                 #
#                                          #
############################################

# Functions to calculate Prevalence, Incidence, Mortality, and Years of life lost

def calculatePrevalence(totalCases, population):
    prevalence = (totalCases / population) * 100000
    return prevalence

def calculateIncidence(newCases, population):
    incidence = (newCases / population) * 100000
    return incidence

def calculateMortality(deaths, population):
    mortality_rate = (deaths / population) * 100000
    return mortality_rate

def calculateLifeLost():
    lifeExpectancy = int(input("Enter the life expectancy: "))
    n = int(input("Amount of age data points: "))
    yearsLost = 0
    for i in range(0, n):
        yearsLost += lifeExpectancy - int(input("Age: "))
    
    print(f"Years of Potential Life Lost: {yearsLost}")

def main():
    totalCases = int(input("Total cases: "))
    population = float(input("Total population: "))
    newCases = int(input("New cases: "))
    deaths = int(input("Deaths: "))

    # Calculating Disease Statistics
    prevalence = calculatePrevalence(totalCases, population)
    incidence = calculateIncidence(newCases, population)
    mortality = calculateMortality(deaths, population)

    # Printing results
    print(f"Illness A Prevalence: {prevalence:.2f} per 100,000")
    print(f"Illness A Incidence: {incidence:.2f} per 100,000")
    print(f"Illness A Mortality Rate: {mortality:.2f} per 100,000")
    
    if input("Calculate Years of Potential Life Lost? (y/n): ") == "y":
        calculateLifeLost()

main()

    

