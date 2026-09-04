'''
In this assignment you will write a program that takes in three inputs (x,y,z) and 
uses the math module to output x to the power of z, x to the power of (y to the power of z), 
the absolute value of (x-y), and the square root of (x to the power of z).

Name: Jeremy Willman
Lab Time: 9/4/2026

'''
import math

def math_func():
    #Type your code here
     x = float(input("Enter a value for x:"))
     y = float(input("Enter a value for y:"))
     z = float(input("Enter a value for z:"))
     #calculations for results
     x_power_z = math.pow(x, z)
     x_power_y_power_z = math.pow(x, math.pow(y, z))
     abs_x_minus_y = abs(x - y)
     sqrt_x_power_z = math.hypot(x, z)  # Using hypot to calculate square root of x^2 + z^2
     print(f"{x_power_z:.2f} {x_power_y_power_z:.2f} {abs_x_minus_y:.2f} {sqrt_x_power_z:.2f}")

if __name__ == "__main__":
    math_func()