for i in range (int(input())):
    n=int(input())
    s=input()
    if s[0] == s[-1] :
        print(1)
    elif s == "".join(sorted(s)) or s == "".join(sorted(s , reverse=True)) :
        print(2)
    else :
        print(1)