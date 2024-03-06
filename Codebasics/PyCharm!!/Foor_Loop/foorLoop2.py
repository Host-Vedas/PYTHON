# for VARIABLE in range(start_point , end_point - 1)
# for i in range(1,10):
    # print(i)
key_location = 'chair'
locations =["garage","living room","chair","closet"]
for i in locations:
    if i == key_location:
        print("Key is found in",i)
        break
    else:
        print("key is not found in ",i)
