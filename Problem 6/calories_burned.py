''' 
Write a program to take in the four inputs and calculate the average calories burned.
Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 

Name: Jeremy Willman
Lab Time: 9/4/2026
'''

def calculate_calories_burned():
    #Type your code here
    #Get input make sure it is numeric
    weight = int(input("What is your weight in pounds? "))
    age_years = int(input("How old are you? "))
    heart_rate = int(input("What is your average heart rate?"))
    time_minutes = int(input("How long did you exercise for in minutes?"))
    #calculations of calories burned
    calories_burned = ((age_years * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time_minutes / 8.368
    #output results
    print(f"Calories burned: {calories_burned:.2f}")
if __name__ == "__main__":
    calculate_calories_burned()