"""
Define a function max_of_three()that takes three numbers as arguments and returns the largest of
them
"""

def maxofthree (x,y,z):
    return max(x,y,z)
x=float(input("Write the first number:"))
y=float(input("Write the second number:"))
z=float(input("Write the third number:"))
ma= maxofthree(x, y, z)
print(ma)
