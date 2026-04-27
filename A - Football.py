from collections import defaultdict
d=defaultdict(int)
for i in range (int(input())):
    s=input()
    d[s]+=1
print(max(d, key=d.get))    
