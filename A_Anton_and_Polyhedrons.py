sum = 0 
for i in range (int(input())):
    s = input()
    if s[0] == "T" :
        sum+=4
    elif s[0] == "C" :
        sum += 6
    elif s[0] == "O" :
        sum += 8
    elif s[0] == "D" :
        sum += 12
    else:
        sum+=20   
print(sum)         
