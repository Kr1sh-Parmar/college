#1.	Write a program to create three dictionaries and concatenate them to create fourth dictionary.

d1={}
d2={}
d3={}
d4={}
for i in range(3):
    key=input("Enter key:")
    value=int(input("Enter value:"))
    d1[key]=value
for i in range(3):
    key=input("Enter key:")
    value=int(input("Enter value:"))
    d2[key]=value
for i in range(3):
    key=input("Enter key:")
    value=int(input("Enter value:"))
    d3[key]=value


d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)