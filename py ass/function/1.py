#1.	Write a program that defines a function count_lower_upper() that accepts a string and calculates the number of uppercase and lowercase alphabets in it. It should return these values as a dictionary. Call this function for some sample string.


def count_lower_upper(s):   
    d={"lower":0,"upper":0}
    for i in s:
        if i.islower():
            d["lower"]+=1
        elif i.isupper():
            d["upper"]+=1
    return d
s="Hello World"
print(count_lower_upper(s))




