#code a math expression parser
#no brackets


def get_type(token):
    if token == '+' or token == '-' or token == '*' or token == '/':
        return "op"
    else:
        return "num"

def get_precedence(token):
    if token == '+' or token == '-':
        return 0
    if token == '*' or token == '/':
        return 1
    

def apply_op(num1, num2, op):
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        return str(num1 + num2)
    if op == '-':
        return str(num2 - num1)
    if op == '*':
        return str(num1 * num2)
    if op == '/':
        return str(num2 / num1)

def expression_parser(expression):
    expression = expression.split(" ")
    nums = []
    ops = []
    num_ops = 0

    for token in expression:
        if get_type(token) == "num":
            nums.append(token)
        if get_type(token) == "op":
            if len(ops) > 0:
                while get_precedence(ops[-1]) >= get_precedence(token):
                    num1 = nums.pop()
                    num2 = nums.pop()
                    op = ops.pop()
                    new_val = apply_op(num1, num2, op)
                    nums.append(new_val)
                    print str(nums) + " " + str(ops)
                    if len(ops) == 0:
                        break

            ops.append(token)
        print str(nums) + " " + str(ops)

    while len(nums) > 1:
        num1 = nums.pop()
        num2 = nums.pop()
        op = ops.pop()
        new_val = apply_op(num1, num2, op)
        nums.append(new_val)
        print nums

    return nums


print expression_parser("2 * 2 * 2 - 1 * 2")

