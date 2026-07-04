for i in range (int(input())):
    n = input()
    small_val = '9'
    for i in n :
        if i < small_val :
            small_val = i
    print (small_val)