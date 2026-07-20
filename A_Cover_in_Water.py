for i in range (int(input())):
    n = int(input())
    s = input()
    found = False
    for i in range (n-2):
        if s[i:i+3] == "..." :
            print(2)
            found = True
            break
            
    if not found:
        print(s.count("."))