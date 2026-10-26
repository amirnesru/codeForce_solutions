n = int(input())
arr = list(map(int, input().split())) 
left = 0
right = n-1
alice = 0
bob = 0
count1 = 0
count2 = 0
while right>= left :
   if alice > bob :
       bob+= arr[right]
       right-=1
       count2+=1
   elif alice < bob :
       alice+=arr[left]
       left+=1
       count1+=1
       
   else :
       if right==left :
           count1+=1
           left+=1
       else:
           alice+=arr[left]
           bob+=arr[right]
           left+=1
           right-=1
           count1+=1
           count2+=1
print (count1,count2)           
           