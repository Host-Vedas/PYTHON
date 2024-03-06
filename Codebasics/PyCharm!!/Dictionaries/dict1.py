# dictionary sample
d = {"tom":9823414671,"rob":9803632984,"tom":98566654}
d1 = {'tom':9823414671,'rob':9803632984,'tom':98566654}
print(d['tom']) # here tom is key and the number is value
print(d1["rob"])
# in list we accesss the value using index

# adding new telephone numbert to the dictoniries
d["sam"] = 7847894794789
# print(d1)
# print(d)
# in dictionary key is important order does not matter

# to delete dictinary element
del d["rob"]
# print("after deete dictionary d -> ")
# print(d)
# for i in d:
    # print("key:",i,"Value",d[i])
# for key in d:
    # print("key:",key,"Value",d[key])
for k,v in d.items():
    print("key:",k,"Value",v)
    
