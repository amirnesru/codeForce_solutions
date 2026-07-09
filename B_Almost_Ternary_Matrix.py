for _ in range(int(input())):
    n, m = map(int, input().split())


    arr1 = [0] * m 
    arr2 = [0] * m
    
    for j in range(m):
        if j % 4 == 0 or j % 4 == 3:
            arr1[j] = 1
        else:
            arr2[j] = 1
            
            
    matrix = [arr1, arr2, arr2, arr1]                 
    
    final_matrix = ((n // 4) * matrix) + matrix[:(n % 4)]
    for row in final_matrix:
        print(*(row))