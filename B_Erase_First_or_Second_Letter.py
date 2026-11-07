for _ in range(int(input())):
    n = int(input())
    s = input()
    ss = set()
    count = 0

    for i in s:
        if i not in ss:
            count += len(ss) + 1
            ss.add(i)
        else:
            count += len(ss)

    print(count)