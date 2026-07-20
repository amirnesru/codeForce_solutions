from collections import Counter
for i in range (int(input())):
    n = int(input())
    person1 = list( input().split())
    person2 = list(input().split())
    person3 = list(input().split())
    total = person1 + person2 + person3
    d = Counter(total)
    val_1=val_2=val_3 = 0
    for i in person1 :
        if d[i] == 1:
            val_1+=3
        elif d[i] == 2:
            val_1+=1
    for i in person2 :
        if d[i] == 1:
            val_2+=3
        elif d[i] == 2:
            val_2+=1
    for i in person3 :
        if d[i] == 1:
            val_3+=3
        elif d[i] == 2:
            val_3+=1
    print(val_1, val_2, val_3)
    
    