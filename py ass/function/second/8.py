def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[1:])

# Example usage
text = "hello world"
length = string_length(text)
print("Length of the string is:", length)
