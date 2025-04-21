#3.	A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string


def count_vowels(s):
    if not s:  
        return 0
    else:
        vowels = 'aeiouAEIOU'
        if s[0] in vowels:  
            return 1 + count_vowels(s[1:])
        else:
            return count_vowels(s[1:])  
        

count_vowels("Hello World")  
