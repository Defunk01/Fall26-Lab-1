'''
Write a program that reads in two integers and prints their quotient 3 times

Name: Jeremy Willman
Lab Time: 8/28/2026

'''
def divide_ints():
    #Type your code here
    #Get input make sure it is numeric
    user_num = int(input("Enter an integer: "))
    div_num = int(input("Enter another integer: "))
    
    # Calculate the quotient
    quotient = user_num // div_num

    # Print the quotient 3 times
    for _ in range(3):
        print(quotient)

if __name__ == "__main__":
    divide_ints()