def check_substring(str1, str2):
    if str1 in str2:
        return f'"{str1}" is in "{str2}"'
    elif str2 in str1:
        return f'"{str2}" is in "{str1}"'
    else:
        return 'Neither string is in the other'

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = check_substring(string1, string2)
print(result)