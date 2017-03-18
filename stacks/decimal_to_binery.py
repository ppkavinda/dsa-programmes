import stack

decimal = 233
s1 = stack.Stack()

while decimal >= 1:
    s1.push(decimal % 2)
    decimal //= 2

s1.printStack()
