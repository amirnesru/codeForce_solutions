s = input()
length = len(s)
res = [0] * length
for i in range (1,length):
    if s[i] == s[i-1]:
        res[i] = res[i-1]+1
    else:
        res[i] = res[i-1]
for i in range (int(input())):
    l, r = map(int, input().split())
    
    print (res[r-1] - res[l-1])
         