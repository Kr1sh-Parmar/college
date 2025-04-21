#4.	A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names beginning with A and another with B.

s=set()
s.add("aaaaaaa")
s.add("bbbbbbb")
s.add("ccccccc")
s.add("a")
s.add("b")
print(s)

a=set()
b=set()
for i in s:
    if i[0]=="a":
        a.add(i)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    elif i[0]=="b":
        b.add(i)
print(a)
print(b)   