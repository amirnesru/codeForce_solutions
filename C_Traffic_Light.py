for _ in range(int(input())):
    n, c = input().split()
    s = input()
    found  = []
    green = []
    ans =[]
    if c == "g":
       print(0)
       continue
    for i in range(len(s)):
        if s[i] == c:
            found.append(i)
    for i in range(len(s)):
        if s[i] == "g" :
            green.append(i)    
    poi1 =0
    poi2 =0
    while poi2 < len(found):
        if green[poi1] > found[poi2] :
            ans.append(green[poi1]- found[poi2])
            
            poi2+=1
        else:
            if poi1+1 < len(green):
                poi1+=1
            else:
                ans.append(len(s)-(found[poi2]-green[0]))
                poi2+=1
    print(max(ans))  
    