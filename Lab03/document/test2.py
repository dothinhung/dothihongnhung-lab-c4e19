# from random import randint, choice

# x = randint(1, 10)
# y = randint(1, 10)
# op = choice(["+", "-", "*", "/"])


# res = 0
# if op == "+":
#     res = x + y
# elif op == "-":
#     res = x - y
# elif op == "*":
#     res = x * y
# elif op == "/":
#     res = x / y

# error = choice([-1, 0, 1])

# display_result = res + error

# print("{0} {1} {2} = {3}".format(x, op, y, display_result))


# ans = input("(Y/N) ? : ")

# if error == 0:
#     if ans == "y":
#         print("yay")
#     elif ans == "n":
#         print("You're wrong")
# else:
#     if ans == "y":
#         print("You're wrong")
#     elif ans == "n":
#         print("yay")


##################
from random import randint, choice
import eval

x = randint(1, 10)
y = randint(1, 10)
op = choice(["+", "-", "*", "/"])

res = eval.calc(x, y, op)

error = choice([-1, 0, 1])
display_result = res + error


print("*" *10)
print("{0} {1} {2} = {3}".format(x, op, y, display_result))
print("*" *10)

ans = input("(Y/N) ? : ").upper()

if error == 0:
    if ans == "y":
        print("yay")
    elif ans == "n":
        print("You're wrong")
elif error != 0:
    if ans == "y":
        print("You're wrong")
    elif ans == "n":
        print("yay")
