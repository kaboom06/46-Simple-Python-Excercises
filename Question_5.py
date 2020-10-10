"""
Write a function translate()that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o"in between. For example, translate("this is fun")should return the string "tothohisos isos fofunon"
"""
def robberslanguage(x):
    answer = ""
    for c in x:
        if c in ('a', 'e', 'i', 'o', 'u'):
            answer=answer+c
        else:
            answer=answer+c+"o"+c
    return answer
x=input("Input a word")
print(robberslanguage(x))
