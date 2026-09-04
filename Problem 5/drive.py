'''
Read in the users milage and cost per gallon of gas. Then output the cost to drive 20, 75, and 500 miles.

Name: Jeremy Willman
Lab Time: 9/4/2026
'''

def drive():
    #Type your code here
    #Get input make sure it is numeric
    miles_per_gallon = float(input("Enter the miles per gallon of your vehicle: "))
    dollars_per_gallon = float(input("Enter the cost per gallon of gas: "))
    #Calculations of 20,75, and 500 miles
    cost_20_mi = (20/miles_per_gallon) * dollars_per_gallon
    cost_75_mi = (75/miles_per_gallon) * dollars_per_gallon
    cost_500_mi = (500/miles_per_gallon) * dollars_per_gallon
    #Output the results
    print(f"{cost_20_mi:.2f} {cost_75_mi:.2f} {cost_500_mi:.2f}")

if __name__ == "__main__":
    drive()