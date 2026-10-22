for i in range (int(input())):
    n = int(input())
    s = input()
    count = 0
    max_val = 0
    for i in range (1,n):
        if s[i-1] == s[i]:
            count+=1
        else:
            max_val = max(max_val,count)
            count = 0
    max_val = max(max_val,count)     
    print(max_val+2)   
        