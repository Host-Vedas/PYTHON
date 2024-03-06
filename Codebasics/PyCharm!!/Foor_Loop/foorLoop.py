exp = [2340,2500,2100,3100,2980]
total = 0
# for item_iteration in exp:
#     total = total +item_iteration
'''
item_iteration = exp[0]
total = 0+2340
item_iteration = exp[1]
total = 2340 + 2500
item_iteration = exp[2]
item_iteration = exp[3]
item_iteration = exp[4]
total = 2340+2500+2100+3100+2980
'''
# print(total)
print("length of list",len(exp))
for i in range (len(exp)):
    print('Month : ',(i+1),'Expense:',exp[i])
    total = total + exp[i]
print("My total expense is -->",total)