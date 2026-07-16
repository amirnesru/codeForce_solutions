for i in range(int(input())):
    n = int(input())
    s = input()
    print(len(set(s))*2 + n - len(set(s)))