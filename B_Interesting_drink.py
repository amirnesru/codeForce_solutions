n = int(input())
price = list(map(int, input().split()))
q = int(input())
price.sort()
for i in range(q):
    m = int(input())
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if m < price[mid]:
            high = mid-1
        else:
            low = mid+1
    print(high+1)