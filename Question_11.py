"""
Define a function generate_n_chars()that takes an integer nand a character cand returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x")should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x"that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)
"""

def generate_n_chars(n,c):
    s = ''.join([c for i in range(n)])
    return s
i = int(input("Please input the number of characters"))
m = input("Please input the Character.")
print(generate_n_chars(i,m))
