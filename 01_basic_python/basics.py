# -------------------------------------
# Lesson 1: Python Basics for AI
# Ice Cream Sales Example
# -------------------------------------

import numpy as np
import pandas as pd

print("Welcome to the Ice Cream Sales Program 🍦")
print("-------------------------------------")

# 1️⃣ VARIABLES
print("\nVARIABLES")

temperature = 30
sales = 150

print("Temperature:", temperature)
print("Ice Cream Sales:", sales)

# 2️⃣ DATA USING NUMPY
print("\nNUMPY DATA")

temperatures = np.array([25, 28, 30, 33, 35])
ice_cream_sales = np.array([100, 120, 150, 200, 240])

print("Temperatures:", temperatures)
print("Ice Cream Sales:", ice_cream_sales)

# 3️⃣ DATA USING PANDAS
print("\nPANDAS DATAFRAME")

data = pd.DataFrame({
    "Temperature": temperatures,
    "Sales": ice_cream_sales
})

print(data)

# 4️⃣ LOOP THROUGH DATA
print("\nLOOP THROUGH DATA")

for i in range(len(temperatures)):
    print("Temperature:", temperatures[i], "→ Sales:", ice_cream_sales[i])

# 5️⃣ CONDITION
print("\nCONDITION CHECK")

today_temperature = 40

if today_temperature > 35:
    print("Very hot day! Expect more ice cream sales 🍦")
else:
    print("Normal weather today.")

# 6️⃣ FUNCTION
print("\nFUNCTION EXAMPLE")

def predict_sales(temp):
    predicted = temp * 5
    return predicted

result = predict_sales(30)
print("Predicted sales for 30°C:", result)

# 7️⃣ CLASS
print("\nCLASS EXAMPLE")

class IceCreamShop:

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome to", self.name)

    def show_data(self):
        print("\nCurrent Sales Data:")
        print(data)

shop = IceCreamShop("Global Village Ice Cream Shop")

shop.welcome()
shop.show_data()

print("\nProgram Finished ✅")