import stack


def balanceP(word):

    s = stack.Stack()
    op = ["(", "[", "{"]
    cl = [")", "]", "}"]

    for char in word:
        if (char in op) or (char in cl):
            if char in op:
                s.push(char)
            else:
                if not s.isEmpty():
                    poped = s.pop()
                    if op.index(poped) != cl.index(char):
                        print("Not matched.1")
                        break
                    else:
                        print("Matched")
                else:
                    print("Not matched.2")
                    break
        else:
            # print("CHAR|", char)
            pass
    if not s.isEmpty():
        # s.printStack()
        print("Not matched.3")
    else:
        print(word, ":>:parentheses are balanced.")


balanceP("()9()32655+({}[])")
balanceP("(()({({({[9[9[()]]]})})})()()())")