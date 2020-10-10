"""
Write a function is_member()that takes a value and a list of values a, and returns True if x is a member of a, otherwise False. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)
"""

def is_member(x):
    numberList = []
    n = int(input("Enter the list size : "))

    print("\n")
    for i in range(0, n):
        item = int(input())
        numberList.append(item)
    i=0
    while i < n:
        if x == numberList[i-1]:
            return True
        i += 1
    return False
x = int(input("Input a value"))
is_member(x)
