"""
Define a function overlapping()that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member()function, or the inoperator, but for the sake of the exercise, you should (also) write it using two nested for loops.
"""

def overlapping(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

x = []
n = int(input("Enter the list size for the first list : "))

print("\n")
for i in range(0, n):
    item = int(input())
    x.append(item)
        
y = []
m = int(input("Enter the list size for the second list: "))

print("\n")
for i in range(0, m):
    item = int(input())
    y.append(item)

a = overlapping(x,y)
print (a)
