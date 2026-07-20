for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input ().split()))
    max_index = arr.index(max(arr))
    min_index = arr. index(min(arr))
    value  = arr[max_index] - arr[min_index]
    arr.pop(max_index)
    if max_index < min_index :
        arr.pop(min_index-1)
    else:
        arr.pop(min_index)

    value += (max(arr)- min(arr))
    print(value)