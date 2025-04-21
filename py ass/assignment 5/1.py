import random

l=[]
k=[]

num=[random.randint(0,100) ]

l.insert(2,k)
l.pop(3)

print(l)
ft = []  

for i in l:
    if type(i) == list: 
        ft.extend(i)   
    else:
        ft.append(i)
         

print(ft)

ft.sort()

print(ft)











