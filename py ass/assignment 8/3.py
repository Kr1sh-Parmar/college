#3.	Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.

s=set()
for i in range(5):
    s.add(input("Enter name: "))
print(s)

s.remove(input("Enter name to modify: "))
s.add(input("Enter new name: "))
print(s)


s.remove(input("Enter name to remove: "))
print(s)

s.remove(input("Enter name to remove: "))

print(s)

