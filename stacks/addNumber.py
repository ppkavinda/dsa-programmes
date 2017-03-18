import stack

# add numbers 592, 3784
s1 = stack.Stack()
s1.push(5)
s1.push(9)
s1.push(2)

s2 = stack.Stack()
s2.push(3)
s2.push(7)
s2.push(8)
s2.push(4)

s3 = stack.Stack()
ans = 0
exe = 0


while not (s1.isEmpty() and s2.isEmpty()):
    if s1.isEmpty():
        x = s2.pop()
        y = 0
    elif s2.isEmpty():
        x = 0
        y = s1.pop()
    else:
        x = s2.pop()
        y = s1.pop()

    ans = x + y + exe

    if ans >= 10:
        ans -= 10
        exe = 1
    else:
        exe = 0

    s3.push(ans)

s3.printStack()

while not s3.isEmpty():
    print(s3.pop(), end='')
