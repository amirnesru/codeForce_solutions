for i in range (int(input())):
    x,y = map(int, input().split())
    a,b = map(int, input().split())
    a_val =(max(x,y) - min(x,y))*a 
    print(min((x+y)*a, (min(x,y) * b + a_val)))