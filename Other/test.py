def candy():
    f_line = input()
    s_line = input()

    t_student = int(f_line.split()[0])
    inc = int((f_line.split())[1])
    candy_line = [0 for x in s_line.split()]
    student_line = [y for y in range(1, t_student+1)]
    val_a = [int(x) for x in s_line.split()]

    while len(val_a) > 1:
        # print(student_line, "b")
        if candy_line[0] >= val_a[0]:
            candy_line.pop(0)
            student_line.pop(0)
            val_a.pop(0)
        else:
            a = candy_line.pop(0) + inc
            candy_line.append(a)
            student_line.append(student_line.pop(0))
            val_a.append(val_a.pop(0))
    print(student_line[0])

candy()