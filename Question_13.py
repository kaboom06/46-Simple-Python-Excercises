"""
The function max()from exercise 1) and the function max_of_three()from exercise 2) will only work for  two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list()that takes a list of numbers and returns the largest one.
"""

def max_in_list(x):
    return max(x)
List = []
n = int(input("Enter the list size : "))
print("Please enter each number one by one.")
for i in range(0, n):
    item = int(input())
    List.append(item)
print ("\n")
print (max_in_list(List))
