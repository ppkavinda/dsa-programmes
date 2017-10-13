def postfix_calculate(exp):  # exp stands for expression

    s = []  # creating stack obj
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for char in exp:  # looping through the expression
        if char in nums:  # char for character
            s.append(char)  # if cha is a number push it to the stack
        else:             # if not pop twice from stack
            num2 = s.pop()
            num1 = s.pop()
            print("LD", num1)

            if char is "+":  # setting the appropriate operation to the popped numbers
                tmp = (float(num1) + float(num2))  # and assign it to the tmp(temporary) variable
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

            s.append(tmp)  # finally push tmp to the stack
            print("ST", tmp)

        # print(char)
        # s.printStack()

postfix_calculate("345+*")
