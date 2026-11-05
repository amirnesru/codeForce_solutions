for i in range(int(input())):
    n = int(input())
    s = input()
    arr = []
    count = 0
    for i in s :
        if i =="(" :
            arr.append(i)
        else:
            if arr :
                arr.pop()
            else:
                count+=1
    print(count)            