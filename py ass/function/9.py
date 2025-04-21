#9.	Write a program that defines a function count_alpha_digits() that accepts a string and calculates the number of alphabets and digits in it. It should return these values as a dictionary.

def count_alpha_digits(s):
    d = {"alphabets":0, "digits":0}
    for ch in s:
        if ch.isalpha():
            d["alphabets"] += 1
        elif ch.isdigit():
            d["digits"] += 1
    return d

s = input("Enter a string: ")
print(count_alpha_digits(s))

