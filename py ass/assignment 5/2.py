import random

n=[]
for i in range(20):
    n.append(random.randint(1,5))

print(n)

num=int(input("Enter a number: "))    


for i in range(20):
    if n[i]==num:
        print(f"The number {num} is present at index {i}")
        

