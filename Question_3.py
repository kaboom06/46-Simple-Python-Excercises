"""
Define a function that computes the length of a given list or string. (It is true that Python has the len()
function built in, but writing it yourself is nevertheless a good exercise.)
"""

def lenght(x):
    counter=0
    for c in x:
        counter=counter+1
    return counter
x=str(input("put your word"))
l=lenght(x)
print(l)
