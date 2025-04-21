#1.	Write a program that converts words present in a list into uppercase and stores them in a set.

words = ["apple", "banana", "cherry", "date"]
words = set(words)
print(words)
word = {x.upper() for x in words}
print(word)