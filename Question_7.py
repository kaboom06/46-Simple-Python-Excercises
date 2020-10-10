"""
Define a function reverse()that computes the reversal of a string. For example, reverse("I am testing")should return the string "gnitset ma I".
"""
def reverse(x):
    answer = ""
    length = len(x)
    counter = 0
    while counter < length:
        answer = answer + x[length-counter-1]
        counter = counter + 1
    return answer
#Main program below
x=str(input("Write something:"))
print(reverse(x))
print (x)
