import operator

l=[("pizza",100),("noodles",300),("burger",200),("pasta",400),("sandwich",500)]
print(sorted(l,key = operator.itemgetter(1),reverse=True))