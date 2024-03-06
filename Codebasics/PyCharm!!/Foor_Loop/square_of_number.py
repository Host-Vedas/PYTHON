# iteration will go from 1 to 5
for i in range(1,6):
# to avoid printing of even numbers we have used continue for even condition ,
    if i%2 == 0:
        print("We have skipped",i)
        continue
        # method 1
    print(i*i)
        # method 2
        # print(i**2)