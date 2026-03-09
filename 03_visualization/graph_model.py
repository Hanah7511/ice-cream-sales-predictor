import numpy as np
import matplotlib.pyplot as plt


print("Ice Cream Sales Visualization 🍦")
print("-------------------------------------")

# dataset
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

        for i in range(len(X)):
            num += (X[i] - mean_x) * (Y[i] - mean_y)
            den += (X[i] - mean_x) ** 2

        self.m = num / den
        self.b = mean_y - self.m * mean_x

    def predict(self, X):
        return self.m * X + self.b


# train model
model = LinearRegressionModel()
model.train(temperatures, sales)

# predictions for line
predicted_sales = model.predict(temperatures)

# graph
plt.scatter(temperatures, sales)
plt.plot(temperatures, predicted_sales)

plt.xlabel("Temperature")
plt.ylabel("Ice Cream Sales")
plt.title("Temperature vs Ice Cream Sales")

plt.show()