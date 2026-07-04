for i in range (int(input())):
    n = int(input())
    row_1 = list(input())
    row_2 = list(input())
    for i in range (n):
        if row_1[i] == "R"  and row_2[i] != "R" or row_1[i] != "R"  and row_2[i] == "R":
            print("NO")
            break
    else :
        print("YES")