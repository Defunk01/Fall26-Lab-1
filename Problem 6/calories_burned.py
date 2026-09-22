''' 
Write a program to take in the four inputs and calculate the average calories burned.
Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 

Name: Jeremy Willman
Lab Time: 9/4/2026
'''

def calculate_calories_burned():
    #Type your code here
    #Get input make sure it is numeric
    Weight = int(input("What is your weight in pounds? "))
    Age = int(input("How old are you? "))
    Heart_Rate = int(input("What is your average heart rate?"))
    Time = int(input("How long did you exercise for in minutes?"))
    #calculations of calories burned
    calories = ((Age * 0.2757) + (Weight * 0.03295) + (Heart_Rate * 1.0781) - 75.4991) * Time / 8.368
    #output results
    print(f"Calories burned: {calories:.2f}")
if __name__ == "__main__":
    calculate_calories_burned()