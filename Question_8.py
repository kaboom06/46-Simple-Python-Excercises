"""
Define a function is_palindrome()that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar")should return True.
"""
def is_palindrome(x):
    answer = ""
    length = len(x)
    counter = 0
    while counter < length:
        answer = answer + x[length-counter-1]
        counter = counter + 1
    return answer
x=str(input("Please write something and i will check wether it is the same when written backwards: "))
if x == is_palindrome(x):
    print ("True")
else:
    print ("False")
