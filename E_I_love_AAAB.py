for _ in range(int(input())):
    s2 = input()
    if len(s2) < 2 or s2[-1] != "B":
        print("NO")
        continue
    count = 0
    possible = True
    for char in s2:
        if char == "A":
            count += 1
        else:
            count -= 1  
        if count < 0: 
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")
