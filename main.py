import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Linear_Regression:

    def __init__(self, file_path):
        
        self.train_data = pd.read_csv(file_path)
        self.train_x = self.train_data.pop("house age")
        self.train_y = self.train_data.pop("house price of unit area")

    
    def Slope_and_Intercept(self):
        
        #Slope
        m = sum(float(x - self.train_x.mean() * (y - self.train_y.mean())) for x, y in zip(self.train_x[0:], self.train_y[0:]))/sum(float(x - self.train_x.mean()**2) for x in self.train_x[0:])
        
        #Intercept
        b = float(self.train_y.mean() - m * self.train_x.mean())

        return m, b
    
    def Drawing_Graph(self, predictions, user_x, user_y):

        plt.xlabel('House Age')
        plt.ylabel('Cost per unit area in $')
        
        # plotting points as a scatter plot
        plt.scatter(self.train_x, self.train_y, color= "blue", marker= ".")

        #best fit line
        plt.plot(self.train_x, predictions, color = "red")

        #predictions
        plt.scatter(user_x, user_y, color = "red")

        plt.annotate("$"+ str(round(user_y, 2)) , xy=(user_x, user_y), xytext=(4, 10), fontsize=12,
            arrowprops=dict(facecolor='green', shrink=0.05))
        plt.show()

    

if __name__ == "__main__":
    #Creating Linear Regression Model
    file_path = "Replace this with file path" 

    model = Linear_Regression(file_path)

    #Generating slope and y inercept
    linear_variables = model.Slope_and_Intercept()

    #generating best fit line
    predictions = [linear_variables[0]*x + linear_variables[1] for x in model.train_x]

    #taking user input for predictions
    user_x  = float(input("Enter house age : "))

    #displaying o/p through graph
    model.Drawing_Graph(predictions , user_x, linear_variables[0]*user_x+linear_variables[1])