for i in range (int(input())):
    n = int(input())
    s = input()
    left = 0
    right = n-1
    counter = 0
    found = True
    while left < right :
        if s[left] == s[right] :
            left +=1
            right -=1
            if counter > 0 :
                counter = 2
        else :
            left +=1
            right -=1
            if counter == 2:
                found = False
                print("No")
                break
            counter = 1
    else :
        if found:
            print("Yes")