#7.	Delete an element of a tuple.

t=(1,2,3,4,5)
t=list(t)
t.remove(3)
t=tuple(t)
print(t)