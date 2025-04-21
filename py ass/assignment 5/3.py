import random

# import random

# n=[]
# for i in range(50):
#     n.append(random.randint(1,30))

# print(n)

# for i in n:
#     for j in n:
#         if i==j:
#             n.remove(j)

n = [random.randint(1, 30) for _ in range(50)]
print(n)
k = list(set(n))

print(k)