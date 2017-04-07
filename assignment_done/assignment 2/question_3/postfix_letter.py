# Implementing the Stack class
# This is Complete


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, ele):
        self.items.append(ele)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def printStack(self):
        print(self.items)

# ///// End of Stack class


def postfix_calculate(exp):  # exp stands for expression

    s = Stack() # creating stack obj
    i = 1

    for char in exp:  # looping through the expression
        if char.isalpha():  # char for character
            s.push(char)  # if cha is a number push it to the stack
        else:             # if not pop twice from stack
            num2 = s.pop()
            num1 = s.pop()
            print("LD", num1)

            if char is "+":  # setting the appropriate operation to the popped numbers
                tmp = "TEMP" + str(i)
                print("AD", num2)

            elif char is "-":
                tmp = "TEMP" + str(i)
                print("SB", num2)

            elif char is "*":
                tmp = "TEMP" + str(i)
                print("MP", num2)

            elif char is "/":
                tmp = "TEMP" + str(i)
                print("DV", num2)

            s.push(tmp) # finally push tmp to the stack
            print("ST", tmp)
            i += 1

postfix_calculate("asd+*")
