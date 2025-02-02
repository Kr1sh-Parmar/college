def count(input_string):
    alphabets = 0
    digits = 0
    
    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
    
    return alphabets, digits

string = input("Enter a string: ")
alphabets, digits = count(string)
print(f"Number of alphabets: {alphabets}")
print(f"Number of digits: {digits}")