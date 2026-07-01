n, k = map(int, input().split())
remainder = 240 - k
sum = 0
count = 0
i = 1
while sum <= remainder :
    
    sum += i*5
    if sum <= remainder :
        count+=1
    i+=1
print (min(count,n))    