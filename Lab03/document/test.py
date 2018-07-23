# x = int(input("x = "))


# operation = input("Operation (+, -, *, /):")
# y = int(input("y = "))


# if operation == "+":
#     sum = x + y
#     print("{0} + {1} = {2}".format(x, y, sum))
# elif operation == "-":
#     result = x - y
#     print("{0} - {1}  = {2}".format(x, y, result))
# elif operation == "*":
#     mul = x*y
#     print("{0} * {1}  = {2}".format(x, y, mul))
# elif operation == "/":
#     dev = x/y
#     print("{0} / {1}  = {2}".format(x, y, dev))


################

x = int(input("x = "))
op = input("Operation (+, -, *, /): ")
y = int(input("y = "))

res = 0

if op == "+":
    res = x + y
elif op== "-":
    res = x - y
elif op == "*":
    res == x * y
elif op == "/":
    res == x / y

print("*" *10)
print("{0} {1} {2} = {3}".format(x, op, y, res))
print("*" *10)