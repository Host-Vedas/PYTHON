def sum(a,b):
    print("a ->",a)
    print("b ->",b)
    total = a+b
    print("Total inside function",total)
    return total
n = sum(5,6)
print("Total outside function : ",n)
