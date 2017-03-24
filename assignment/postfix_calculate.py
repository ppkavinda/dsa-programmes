import stack


def postfix_calculate(exp):
    s = stack.Stack()
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    "345 + *"
    for char in exp:
        if char in nums:
            s.push(char)
        else:
            num2 = s.pop()
            num1 = s.pop()
            print("LD", num1)

            if char is "+":
                tmp = (float(num1) + float(num2))
                print("AD", num2)
            elif char is "-":
                tmp = (float(num1) - float(num2))
                print("SB", num2)
            elif char is "*":
                tmp = (float(num1) * float(num2))
                print("MP", num2)
            elif char is "/":
                tmp = (float(num1) / float(num2))
                print("DV", num2)

            s.push(tmp)
            print("ST", tmp)

        # print(char)
        # s.printStack()

postfix_calculate("345+*")
