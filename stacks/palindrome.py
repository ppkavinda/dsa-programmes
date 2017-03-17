import stack


def palindrome(word):
    s1 = stack.Stack()
    st = ""

    for char in word:
        s1.push(char)

    while not s1.isEmpty():
        st += s1.pop()

    if word == st:
        print(word, " > is a palindrome.")
    else:
        print(word, " is not a palindrome.")

palindrome("101")
