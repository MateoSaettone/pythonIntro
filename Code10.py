############################################
#                                          #
#      Hospital Patient Data Analysis      #
#                                          #
#          Mateo Saettone Ascenzo          #
#               U56111212                  #
#                                          #
############################################

# import packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# load data into dataframe
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    'BloodPressure': [120, 122, 126, 128, 130, 133, 135, 138, 142, 145, 150, 155, 160, 165, 170, 175]
}
df = pd.DataFrame(data)

# basic data check
print("summary stats:")
print(df.describe())

print("\nmissing values:")
print(df.isnull().sum())

# scatter plot age vs blood pressure
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['BloodPressure'], color='blue', label='data points')
plt.xlabel('age')
plt.ylabel('blood pressure')
plt.title('age vs blood pressure')
plt.grid(True)

# linear regression model
X = df[['Age']]  # predictor
y = df['BloodPressure']  # response

regression_model = LinearRegression()
regression_model.fit(X, y)

# regression coefficients
intercept = regression_model.intercept_
slope = regression_model.coef_[0]
print(f"\nregression coefficients:")
print(f"intercept (b0): {intercept}")
print(f"slope (b1): {slope}")

# regression line on plot
x_range = np.linspace(df['Age'].min(), df['Age'].max(), 100)
x_range_df = pd.DataFrame({'Age': x_range})  # create DataFrame with same column name
y_pred_line = regression_model.predict(x_range_df)
plt.plot(x_range, y_pred_line, color='red', label='regression line')
plt.legend()
plt.show()

# predictions for example ages
example_ages_df = pd.DataFrame({'Age': [30, 40, 50, 60]})
predicted_bp = regression_model.predict(example_ages_df)

print("\npredicted blood pressure for example ages:")
for age, bp in zip(example_ages_df['Age'], predicted_bp):
    print(f"age: {age} years -> predicted blood pressure: {bp:.2f} mmHg")



