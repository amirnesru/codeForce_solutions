for _ in range(int(input())):
    s = input()
    ss = []
    upper_s = []
    lower_s = []
    for i in s:
        if i == "B":
            if upper_s:
                ss[upper_s.pop()] = ""
        elif i == "b":
            if lower_s:
                ss[lower_s.pop()] = ""
        else:
            ss.append(i)
            if i.isupper():
                upper_s.append(len(ss) - 1)
            else:
                lower_s.append(len(ss) - 1)
    print("".join(ss))