def q6():
    num=int(input("enter no"))
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1

    print ("no of digits",count)
