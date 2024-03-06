tom_expense_list = [2100,3400,3500]
joe_expense_list = [200,700,500]
total = 0
# for item in tom_expense_list:
#     total = total + item
# print("Tom's total expenses : ",total)
# total = 0
# for item in joe_expense_list:
#     total = total +item
# print("Joe's total expenses is : ",total)

def calculate_total (exp):
    total =0
    for item in exp:
        total = total + item
    return total
tom_total =calculate_total(tom_expense_list)
joes_total = calculate_total(joe_expense_list)
print("Tom's total expenses : ",tom_total)
print("Joe's total expenses is : ",joes_total)

