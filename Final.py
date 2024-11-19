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
    # read data from Hospital1.txt into dataframe
    try:
        df1 = pd.read_csv('Hospital1.txt', sep=',', skipinitialspace=True)
    except FileNotFoundError:
        print("Error: Hospital1.txt not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading Hospital1.txt: {e}")
        return

    # read data from Hospital2.txt into dataframe
    try:
        df2 = pd.read_csv('Hospital2.txt', sep=',', skipinitialspace=True)
    except FileNotFoundError:
        print("Error: Hospital2.txt not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading Hospital2.txt: {e}")
        return

    # analyze Hospital 1
    print("Hospital Comparison:")
    print("--------------------\n")

    print("Hospital 1 Data Analysis:")
    print("----------------------")

    # calculate number of patients readmitted in Hospital 1
    numReadmitted1 = df1['Readmission'].sum()
    print(f"Number of Patients Readmitted: {numReadmitted1}\n")

    # calculate average satisfaction scores in Hospital 1
    categories = ['StaffSatisfaction', 'CleanlinessSatisfaction', 'FoodSatisfaction',
                  'ComfortSatisfaction', 'CommunicationSatisfaction']
    for category in categories:
        avgScore = df1[category].mean()
        print(f"Average {category.replace('Satisfaction', '')} Satisfaction: {avgScore:.2f}")

    # calculate overall satisfaction score for Hospital 1
    df1['OverallSatisfaction'] = df1[categories].mean(axis=1)

    # prepare data for logistic regression for Hospital 1
    X1 = df1[['OverallSatisfaction']]  # predictor
    y1 = df1['Readmission']  # response

    # logistic regression model for Hospital 1
    logisticModel1 = LogisticRegression()
    logisticModel1.fit(X1, y1)

    # get coefficient and intercept for Hospital 1
    intercept1 = logisticModel1.intercept_[0]
    coefficient1 = logisticModel1.coef_[0][0]

    # print logistic regression results for Hospital 1
    print("\nLogistic Regression Results:")
    print("----------------------------")
    print(f"Intercept: {intercept1:.4f}")
    print(f"Coefficient: {coefficient1:.4f}")

    # check correlation based on coefficient for Hospital 1
    if coefficient1 > 0:
        correlation1 = "Positive correlation"
    elif coefficient1 < 0:
        correlation1 = "Negative correlation"
    else:
        correlation1 = "No correlation"
    print(f"Correlation between Overall Satisfaction Scores and Readmission: {correlation1}\n")

    # plot data points and logistic regression curve for Hospital 1
    plt.figure(figsize=(8, 6))
    plt.scatter(df1['OverallSatisfaction'], df1['Readmission'], color='blue', label='data points')

    # create range of overall satisfaction scores for plotting
    xPlot1 = np.linspace(df1['OverallSatisfaction'].min(), df1['OverallSatisfaction'].max(), 100)
    xPlot1 = pd.DataFrame(xPlot1, columns=['OverallSatisfaction'])  # add column name

    # predict probabilities for plotting
    yPredProb1 = logisticModel1.predict_proba(xPlot1)[:, 1]

    plt.plot(xPlot1['OverallSatisfaction'], yPredProb1, color='red', label='logistic regression curve')
    plt.xlabel('overall satisfaction score')
    plt.ylabel('probability of readmission')
    plt.title('Logistic Regression: Hospital 1')
    plt.legend()
    plt.grid(True)
    plt.show()

    # analyze Hospital 2
    print("Hospital 2 Data Analysis:")
    print("----------------------")

    # calculate number of patients readmitted in Hospital 2
    numReadmitted2 = df2['Readmission'].sum()
    print(f"Number of Patients Readmitted: {numReadmitted2}\n")

    # calculate average satisfaction scores in Hospital 2
    for category in categories:
        avgScore = df2[category].mean()
        print(f"Average {category.replace('Satisfaction', '')} Satisfaction: {avgScore:.2f}")

    # calculate overall satisfaction score for Hospital 2
    df2['OverallSatisfaction'] = df2[categories].mean(axis=1)

    # prepare data for logistic regression for Hospital 2
    X2 = df2[['OverallSatisfaction']]  # predictor
    y2 = df2['Readmission']  # response

    # logistic regression model for Hospital 2
    logisticModel2 = LogisticRegression()
    logisticModel2.fit(X2, y2)

    # get coefficient and intercept for Hospital 2
    intercept2 = logisticModel2.intercept_[0]
    coefficient2 = logisticModel2.coef_[0][0]

    # print logistic regression results for Hospital 2
    print("\nLogistic Regression Results:")
    print("----------------------------")
    print(f"Intercept: {intercept2:.4f}")
    print(f"Coefficient: {coefficient2:.4f}")

    # check correlation based on coefficient for Hospital 2
    if coefficient2 > 0:
        correlation2 = "Positive correlation"
    elif coefficient2 < 0:
        correlation2 = "Negative correlation"
    else:
        correlation2 = "No correlation"
    print(f"Correlation between Overall Satisfaction Scores and Readmission: {correlation2}\n")

    # plot data points and logistic regression curve for Hospital 2
    plt.figure(figsize=(8, 6))
    plt.scatter(df2['OverallSatisfaction'], df2['Readmission'], color='blue', label='data points')

    # create range of overall satisfaction scores for plotting
    xPlot2 = np.linspace(df2['OverallSatisfaction'].min(), df2['OverallSatisfaction'].max(), 100)
    xPlot2 = pd.DataFrame(xPlot2, columns=['OverallSatisfaction'])  # add column name

    # predict probabilities for plotting
    yPredProb2 = logisticModel2.predict_proba(xPlot2)[:, 1]

    plt.plot(xPlot2['OverallSatisfaction'], yPredProb2, color='red', label='logistic regression curve')
    plt.xlabel('overall satisfaction score')
    plt.ylabel('probability of readmission')
    plt.title('Logistic Regression: Hospital 2')
    plt.legend()
    plt.grid(True)
    plt.show()

    # compare results
    print("Hospital Comparison:")
    print("--------------------\n")

    # Compare readmission rates
    if numReadmitted1 < numReadmitted2:
        readmissionComparison = "Hospital 1 has fewer readmissions."
    elif numReadmitted1 > numReadmitted2:
        readmissionComparison = "Hospital 2 has fewer readmissions."
    else:
        readmissionComparison = "Both hospitals have the same number of readmissions."

    # Compare average satisfaction
    avgSat1 = df1[categories].mean().mean()
    avgSat2 = df2[categories].mean().mean()
    if avgSat1 > avgSat2:
        satisfactionComparison = "Hospital 1 has higher average satisfaction."
    elif avgSat1 < avgSat2:
        satisfactionComparison = "Hospital 2 has higher average satisfaction."
    else:
        satisfactionComparison = "Both hospitals have the same average satisfaction."

    # Compare correlations
    if correlation1 == correlation2:
        correlationComparison = f"Both hospitals have {correlation1}."
    else:
        correlationComparison = f"Hospital 1 has {correlation1}, while Hospital 2 has {correlation2}."

    print(f"Readmission Comparison: {readmissionComparison}")
    print(f"Satisfaction Comparison: {satisfactionComparison}")
    print(f"Correlation Comparison: {correlationComparison}\n")

    # provide conclusion
    print("Conclusion:")
    print("-----------")
    # simple analysis based on the comparisons
    if avgSat1 > avgSat2 and numReadmitted1 < numReadmitted2:
        conclusion = "Hospital 1 may be doing better in terms of patient satisfaction and readmission rates."
    elif avgSat1 < avgSat2 and numReadmitted1 > numReadmitted2:
        conclusion = "Hospital 2 may be doing better in terms of patient satisfaction and readmission rates."
    else:
        conclusion = "Both hospitals perform similarly, or the results are mixed."
    print(conclusion)

if __name__ == '__main__':
    main()
