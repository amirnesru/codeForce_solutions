n = int(input())
s = input()

arr = [0]*10
for i in s:
    if i == "L" :
        arr[arr.index(0)]=1
    elif i =="R" :
        arr[9-arr[::-1].index(0)] = 1
        
    else:
        arr[int(i)] = 0
print ("".join(map(str,arr)) )         