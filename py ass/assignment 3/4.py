def remove_substring(onestring, removestring):
    finalstring = onestring.replace(removestring, "")
    return finalstring

onestring = input("Enter the first string: ")
removestring = input("Enter the second string: ")
finalstring = remove_substring(onestring, removestring)
print(finalstring)