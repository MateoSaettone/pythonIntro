############################################
#                                          #
#         Simple Linear Regression         #
#                                          #
#          Mateo Saettone Ascenzo          #
#               U56111212                  #
#                                          #
############################################

# function to calculate the mean of a list of numbers
def calculate_mean(data):
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
    return total / count

# function to calculate the slope and intercept for the regression line
def calculate_regression_coefficients(data_points):
    # first, we split the data points into x and y values
    x_values = []
    y_values = []
    
    for point in data_points:
        x_values.append(point[0])
        y_values.append(point[1])
    
    # now, we calculate the averages of x and y (x_mean and y_mean)
    x_mean = calculate_mean(x_values)
    y_mean = calculate_mean(y_values)
    
    # we'll need these for the slope calculation
    numerator = 0
    denominator = 0
    
    # calculate both numerator and denominator for the slope formula
    for i in range(len(data_points)):
        x = x_values[i]
        y = y_values[i]
        numerator += (x - x_mean) * (y - y_mean)
        denominator += (x - x_mean) ** 2
    
    # now we can calculate the slope (m)
    slope = numerator / denominator
    
    # and then we calculate the intercept (b)
    intercept = y_mean - (slope * x_mean)
    
    return slope, intercept

# function to make predictions using the slope and intercept
def make_predictions(slope, intercept, x_value):
    return slope * x_value + intercept

# main function where we put everything together
def main():
    # data points: x is the year and y is the life expectancy
    data_points = [
        (2000, 72.5), (2001, 73.1), (2002, 73.8), (2003, 74.2), (2004, 74.7),
        (2005, 75.3), (2006, 75.9), (2007, 76.5), (2008, 76.9), (2009, 77.4),
        (2010, 78.0), (2011, 78.5), (2012, 79.0), (2013, 79.5), (2014, 80.0),
        (2015, 80.5), (2016, 81.0), (2017, 81.5), (2018, 82.0), (2019, 82.5)
    ]
    
    # calculate the slope and intercept from the data
    slope, intercept = calculate_regression_coefficients(data_points)
    
    # print out the slope and intercept values
    print(f"Regression Coefficients:")
    print(f"Slope (m): {slope}")
    print(f"Intercept (b): {intercept}")
    
    # ask the user for a new x value (a year) to make a prediction
    x_value = float(input("Enter a new x value for prediction: "))
    
    # make the prediction based on the given x value
    predicted_y = make_predictions(slope, intercept, x_value)
    
    # display the predicted y value (life expectancy)
    print(f"Predicted y value: {predicted_y}")

# run the main function
main()
