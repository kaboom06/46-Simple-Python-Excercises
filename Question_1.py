"""
Define a function max()  that takes two numbers as arguments and returns the largest of them. Use the if, then and else construct available
in Python. (It is true that Python has the max()  function built in, but writing it yourself is nevertheless a good exercise.)
"""

def max(x, y):
    if x>y:
        return x
    else:
        y>x
        return y
x=float(input("Input first value"))
y=float(input("Input second value"))
ans= max(x,y)
print(ans)
