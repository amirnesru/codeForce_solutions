for i in range (int(input())):
    n = int(input())
    s = input()
    count = 1
    for i in range(len(s)-1) :
        if s[i] != s[i+1] :
            count += 1
    if s[0] != s[-1] and count != len(s):
        count+=1  
    print(count)    

   