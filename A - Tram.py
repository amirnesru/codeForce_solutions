n = int(input())
s = 0
max_val = 0
for i in range(n):
    exi,ent=map(int,input().split())
    s=s-exi+ent
    max_val = max(max_val,s)

print(max_val)
