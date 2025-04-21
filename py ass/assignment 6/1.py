def count_boys_and_girls(names_list):
    b_count = 0
    g_count = 0

    for name in names_list:
        if isinstance(name, tuple):
            b_count += 1
        else:
            g_count += 1

    return b_count, g_count


names = [("krish",), "yug", ("ronit",), "deepika padukon", ("tanmay",), "elizbeth"]
boys, girls = count_boys_and_girls(names)
print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")