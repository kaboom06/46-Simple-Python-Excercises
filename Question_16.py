"""
Write a function filter_long_words()that takes a list of words and an integer nand returns the list of words that are longer than n.
"""

def find_longest_word(word_list):
    word_length = [len(word) for word in word_list]
    return max(word_length)
word_list = []
n = int(input("Enter the list size : "))
print("Please enter each word one by one.")
for i in range(0, n):
    item =input()
    word_list.append(item)
print ("\n")
print (find_longest_word(word_list))
