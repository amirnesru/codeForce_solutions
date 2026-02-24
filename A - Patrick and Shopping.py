distance=list(map(int , input().split()))
distance.sort()
if (distance[0]+distance[1])>distance[2]:
    print(sum(distance))
else:
    print(2*(distance[0]+distance[1]))
