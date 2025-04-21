def copy_uppercase():
    with open("source.txt") as src, open("dest.txt", "w") as dest:
        for line in src:
            dest.write(line.upper())


