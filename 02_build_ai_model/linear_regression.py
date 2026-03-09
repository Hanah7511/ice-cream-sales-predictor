# -------------------------------------
# Lesson 2: Build a Linear Regression AI
# Ice Cream Sales Predictor
# -------------------------------------

import numpy as np


print("Ice Cream Sales AI Model 🍦")
print("-------------------------------------")


# DATASET
temperatures = np.array([25, 28, 30, 33, 35])
sales = np.array([100, 120, 150, 200, 240])


class LinearRegressionModel:

    def __init__(self):
        self.m = 0
        self.b = 0


    def train(self, X, Y):

        mean_x = np.mean(X)
        mean_y = np.mean(Y)

        num = 0
        den = 0

        # loop through data
        for i in range(len(X)):
            num += (X[i] - mean_x) * (Y[i] - mean_y)
            den += (X[i] - mean_x) ** 2

        self.m = num / den
        self.b = mean_y - self.m * mean_x


    def predict(self, temp):

        prediction = self.m * temp + self.b
        return prediction


# create model
model = LinearRegressionModel()

# train model
model.train(temperatures, sales)

print("\nModel trained successfully")

# print learned parameters
print("m =", model.m)
print("b =", model.b)


# make prediction
temp = int(input("Enter today's temperature: "))

if temp < 20 or temp > 45:
    print("Temperature outside normal range!")
else:
    prediction = model.predict(temp)
    print("Predicted Ice Cream Sales:", round(prediction))



