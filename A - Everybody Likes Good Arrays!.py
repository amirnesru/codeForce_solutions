t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    j = 0
    
    while j < len(arr) - 1:
        if arr[j] % 2 == arr[j+1] % 2:
            arr[j] *= arr[j+1]
            arr.pop(j+1)
            count += 1
        else:
            j += 1
    
    print(count)
