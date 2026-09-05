for i in range (int (input())):
    n = int(input())
    arr = list(map(int,input().split()))
    maximum = max(arr)
    count_max = arr.count(maximum) 
    minimum = min(arr)
    count_min = arr.count(minimum) 
    if maximum == minimum :
        print(n * (n - 1))
        
    else:
        print(2*count_max*count_min)