#4.	Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string. 

s=input("Enter a string:")
d={

}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    
print(d)