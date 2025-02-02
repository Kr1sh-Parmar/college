def q13():
    num=input("enter no")
    words=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"] 
    if num in words:
        print(words.index(num))
    else:
        print("not in range")
