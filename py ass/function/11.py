#11.	Write a function create_list() that creates and returns a list which is an intersection of two lists passed to it.

def create_list(l1,l2):
    return [x for x in l1 if x in l2]

l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]
print(create_list(l1,l2))

