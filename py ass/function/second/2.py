#2.	A positive integer is entered through the keyboard. Write a function to find its binary equivalent of this number.

def binary(n):
    if n == 0:
        return ""
    return binary(n//2) + str(n%2)

n = int(input("Enter a number: "))
print(binary)





