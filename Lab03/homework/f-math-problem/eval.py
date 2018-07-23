# define function
# function agruments
def calc(x, y, op):
    res = 0
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
    elif op == "/":
        res = x / y

    return res
    
# #call
# res = calc(1, 2, "+")
# print(res)