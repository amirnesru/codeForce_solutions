for i in range (int(input())):
    s = input() 
    count_ab = 0
    count_ba =0
    for i in range(len(s)-1):
        if s[i:i+2] == "ab" :
            count_ab+=1
        elif  s[i:i+2] == "ba" :
            count_ba+=1
    if count_ba == count_ab :
        print(s)
    elif count_ba >count_ab:
        print("a"+s[1:])
    else:
        print("b"+s[1:])