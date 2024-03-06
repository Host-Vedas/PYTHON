num = input("Enter number")
print("Type of num",type(num))
# input function take/accept all argument/expression as string
num = int(num)
print("Type of num is now upgraded",type(num))
if num%2 == 0:
    print("Even number")
else:
    print("odd number")
