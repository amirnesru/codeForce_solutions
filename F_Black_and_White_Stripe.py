for i in range (int(input())):
    n,k = map(int, input().split())
    s= input() 
    count = s[:k].count("B")
    max_val = count
  
    for i in range (k,n):
        if s[i-k] == "B":
            count-=1
        if s[i] == "B":
            count+=1
        max_val=(max(count,max_val))    
    print(max(0,k-max_val) )  