""""
Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

Expected Output:
For example, if the function is called with 5, it should return:
"""
def fact_rec(num):
    #base condition
     if num==1:
         return 1
     else:
         factorial = num*fact_rec(num-1)
         return factorial
n=int(input("Enter the number you want to see the  factorial for : "))
print(f"The factorial for {n} n is  : ",fact_rec(n))