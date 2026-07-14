n= int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

if sum(list(set(x[1:]+y[1:]))) == ((n*(n+1))//2):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

