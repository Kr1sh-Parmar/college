from itertools import zip_longest

def merge_files():
    with open("file1.txt") as f1, open("file2.txt") as f2, open("merged.txt", "w") as out:
        for line1, line2 in zip_longest(f1, f2, fillvalue=''):
            out.write(line1 + line2)