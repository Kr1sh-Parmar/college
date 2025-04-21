def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

# Example usage
a = 2
b = 3
result = power(a, b)
print(f"{a}^{b} =", result)
