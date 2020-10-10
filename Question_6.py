"""
Define a function sum()and a function multiply()that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4])should return 10, and multiply([1, 2, 3, 4])should return 24.
"""

def sum(list):
    length = len(list)
    answer1 = 0
    for i in range(answer1, length):
        answer1 += list[i]
    return answer1
lst = []
n = int(input("Enter the list size : "))
print("Please enter each number one by one.")
for i in range(0, n):
    item = int(input())
    lst.append(item)
sumlst = sum(lst)
print (sumlst)

def multiply(list):
    length = len(list)
    answer1 = 0
    for i in range(answer1, length):
        answer1 += list[i]
    return answer1
lst1 = []
n1 = int(input("Enter the list size : "))
print("Please enter each number one by one.")
for i in range(0, n1):
    item = int(input())
    lst1.append(item)
print (multiply(lst1))
