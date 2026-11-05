for i in range(int(input())):
    n, j, k = map(int,input().split())
    j-=1
    k-=1
    arr1 = ["12", "21"]
    arr2 = ["123", "132", "213", "231", "312", "321"]
    arr3 = [
        "1234", "1243", "1324", "1342", "1423", "1432",
        "2134", "2143", "2314", "2341", "2413", "2431",
        "3124", "3142", "3214", "3241", "3412", "3421",
        "4123", "4132", "4213", "4231", "4312", "4321"
    ]
    if n == 12 :
        count = 0
        for i in range(2):
            if arr1[j][i] == arr1[k][i]:
                count+=1
        print(f"{count}A{2-count}B")
    elif n == 123 :
            count = 0
            for i in range(3):
                if arr2[j][i] == arr2[k][i]:
                    count+=1
            print(f"{count}A{3-count}B")    
    elif n == 1234 :
            count = 0
            for i in range(4):
                if arr3[j][i] == arr3[k][i]:
                    count+=1
            print(f"{count}A{4-count}B")        
   