import random

random_numbers = [random.randint(-100, 100) for _ in range(30)]

p_num = [num for num in random_numbers if num > 0]
n_num = [num for num in random_numbers if num < 0]

print("Random Numbers:", random_numbers)
print("Positive Numbers:", p_num)
print("Negative Numbers:", n_num)