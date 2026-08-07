for i in range (int(input())):
    s =  input()
    s = list(s)
    s.append("u")
    count = 0 
    before = "u"
    for i in range(len(s)):
        if before == "u" and s[i] == "u" :
            s[i] = s
            count+=1
        before = s[i]
    print(count)