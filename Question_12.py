"""
Define a procedure histogram()that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7])should print the following:
****
*********
*******
none
"""

def histogram(list_var):
    for i in list_var:
        print('*'*i)
List = []
n = int(input("Enter the list size : "))
print("Please enter each number one by one.")
for i in range(0, n):
    item = int(input())
    List.append(item)
print("\n")
print (histogram(List))
