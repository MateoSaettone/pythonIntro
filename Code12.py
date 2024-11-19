############################################
#                                          #
#      Hospital Patient Data Analysis      #
#                                          #
#          Mateo Saettone Ascenzo          #
#                U56111212                 #
#                                          #
############################################

# import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

def main():
    # read data from txt file into dataframe
    try:
        df = pd.read_csv('Week14Assignment.txt', sep=',', skipinitialspace=True)
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # calculate number of patients readmitted
    numReadmitted = df['Readmission'].sum()
    print(f"Number of Patients Readmitted: {numReadmitted}\n")

    # calculate average satisfaction scores
    categories = ['StaffSatisfaction', 'CleanlinessSatisfaction', 'FoodSatisfaction',
                  'ComfortSatisfaction', 'CommunicationSatisfaction']
    for category in categories:
        avgScore = df[category].mean()
        print(f"Average {category.replace('Satisfaction', '')} Satisfaction: {avgScore:.2f}")

    # calculate overall satisfaction score
    df['OverallSatisfaction'] = df[categories].mean(axis=1)

    # prepare data for logistic regression
    X = df[['OverallSatisfaction']]  # predictor
    y = df['Readmission']  # response

    # logistic regression model
    logisticModel = LogisticRegression()
    logisticModel.fit(X, y)

    # get coefficient and intercept
    intercept = logisticModel.intercept_[0]
    coefficient = logisticModel.coef_[0][0]

    # print logistic regression results
    print("\nLogistic Regression Results:")
    print(f"Intercept: {intercept:.4f}")
    print(f"Coefficient: {coefficient:.4f}")

    # check correlation based on coefficient
    if coefficient > 0:
        correlation = "Positive correlation"
    elif coefficient < 0:
        correlation = "Negative correlation"
    else:
        correlation = "No correlation"
    print(f"Correlation between Overall Satisfaction Scores and Readmission: {correlation}")

    # plot data points and logistic regression curve
    plt.figure(figsize=(8, 6))
    plt.scatter(df['OverallSatisfaction'], df['Readmission'], color='blue', label='data points')

    # create range of overall satisfaction scores for plotting
    xPlot = np.linspace(df['OverallSatisfaction'].min(), df['OverallSatisfaction'].max(), 100)
    xPlot = pd.DataFrame(xPlot, columns=['OverallSatisfaction'])  # add column name

    # predict probabilities for plotting
    yPredProb = logisticModel.predict_proba(xPlot)[:, 1]

    plt.plot(xPlot['OverallSatisfaction'], yPredProb, color='red', label='logistic regression curve')
    plt.xlabel('overall satisfaction score')
    plt.ylabel('probability of readmission')
    plt.title('logistic regression: satisfaction vs. readmission')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
