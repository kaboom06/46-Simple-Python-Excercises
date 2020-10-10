"""
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, otherwise false
"""

print("This program detects wheather your character is a vowel or not.")
def voweldetector(x):
    for c in x:
        if c in ('a', 'e', 'i', 'o', 'u'):
            return True
        else:
            return False
    return ans
x=input("Put 1 character")
print(voweldetector(x))
