#4.	Write a recursive function that reverses the list of numbers that it receives.


def reverse_list(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_list(lst[:-1])
    

    

reverse_list([1, 2, 3, 4, 5])

reverse_list([1, 2, 3, 4, 5, 6])