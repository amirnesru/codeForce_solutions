s=input()
left=0
while left< len(s):
    if s[left]==".":
        print(0,end="")
        left+=1
    elif s[left]=="-" and s[left+1]==".":
        print(1,end="")
        left+=2
    else:
        print(2,end="")
        left+=2        
