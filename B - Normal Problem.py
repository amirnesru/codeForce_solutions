for _ in range(int(input())):
    a=input()
    b=""
    for ch in a:
        if ch =="q":
            b+="p"
        elif ch=="p":
            b+="q"
        else:
            b+="w"
    print(b[::-1])        
