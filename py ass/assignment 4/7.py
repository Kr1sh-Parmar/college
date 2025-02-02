def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    return factorial(n) // factorial(n - r)


n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"nCr({n}, {r}) = {nCr(n, r)}")
print(f"nPr({n}, {r}) = {nPr(n, r)}")