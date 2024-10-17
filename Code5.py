############################################
#                                          #
#           Systematic Sampling            # 
#                                          #
#          Mateo Saettone Ascenzo          #
#                U56111212                 #
#                                          #
############################################

import math

# function to calculate the sample size
def calculate_sample_size(population_size, confidence_level, margin_of_error):
    # pick the z-score based on confidence level
    if confidence_level == 90:
        z = 1.645
    elif confidence_level == 95:
        z = 1.96
    elif confidence_level == 98:
        z = 2.33
    elif confidence_level == 99:
        z = 2.576
    else:
        print("Invalid confidence level. Please use 90, 95, 98, or 99.")
        return -1

    p = 0.5  # use 0.5 as a safe estimate if you don't know the actual proportion
    e = margin_of_error

    # calculate sample size with the formula
    sample_size = (z**2 * p * (1 - p)) / (e**2)

    # if sample size is more than population, set it to population size
    if sample_size > population_size:
        sample_size = population_size

    # round up to the nearest whole number
    return math.ceil(sample_size)

# function to actually do the sampling
def systematic_sampling(population, sample_size):
    interval = round(len(population) / sample_size)  # calculate interval and round
    sample = []

    # loop through the population with the calculated step
    for i in range(0, len(population), interval):
        sample.append(population[i])

        # stop once we've reached the sample size needed
        if len(sample) >= sample_size:
            break

    return sample

# main function to get input from user and run sampling
def main():
    # get the size of the population and sampling preferences
    population_size = int(input("Enter the population size: "))
    confidence_level = int(input("Enter the confidence level (e.g., 90, 95, 98, or 99): "))
    margin_of_error = float(input("Enter the desired margin of error (e.g., 0.05 for 5%): "))

    # calculate sample size based on the inputs
    required_sample_size = calculate_sample_size(population_size, confidence_level, margin_of_error)

    if required_sample_size == -1:
        return

    print(f"\nThe required sample size for systematic sampling is approximately {required_sample_size}.")

    # make a population list as a range
    population = list(range(1, population_size + 1))  # a list of numbers as the population

    # ask the user for the sample size they want to take
    requested_sample_size = int(input("\nEnter the sample size you want to draw: "))

    # if they ask for too much, tell them and ask again
    while requested_sample_size > required_sample_size:
        print(f"Sorry, the requested sample size is not feasible with the given population size, confidence level, and margin of error.")
        print(f"The maximum sample size possible is {required_sample_size}. Please enter a lower value.")
        requested_sample_size = int(input("\nEnter the sample size you want to draw: "))

    # do the sampling
    sample = systematic_sampling(population, requested_sample_size)
    print(f"\nThe systematic sampling selected the following elements:\n{sample}")

# run the main function
main()
