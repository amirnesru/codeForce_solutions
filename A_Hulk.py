n = int(input())
odd ="I hate that "
last_odd = "I hate it"
even = "I love that "
last_even = "I love it"
for i in range (1,n+1):
    if i == n and i%2 == 1:
        print(last_odd)
        
    elif i == n and i%2 == 0:
        print(last_even)
    
    elif i%2 == 1 :
        print(odd, end="")
    else:
        print(even, end="")