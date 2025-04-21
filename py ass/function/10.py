#10.	Write a program that defines a function called frequency() which computes the frequency of words present in a string passed to it. The frequencies should be returned in sorted order of words in the string.

def frequency(s):
    words = s.split()
    d = {}
    for word in words:
        d[word] = d.get(word, 0) + 1
    return sorted(d.items())

s = input("Enter a string: ")
print(frequency(s))

