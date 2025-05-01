import sys
input = sys.stdin.readline

cookie = []
heart = None
body=0
left_leg=0
right_leg=0
n = int(input())

for i in range(n):
    cookie.append(list(map(str,input().rstrip())))

for i in range(n):
    if "*" in cookie[i]: 
        head = cookie[i].index("*")
        heart = (i+1,head)
        print(heart[0]+1,heart[1]+1)
        break
    
left_arm=cookie[heart[0]][:heart[1]].count("*")
right_arm=cookie[heart[0]][heart[1]+1:].count("*")



for i in range(heart[0]+1,n):
    if cookie[i][heart[1]] == "*":
        body+=1
    if cookie[i][heart[1]-1] == "*":
        left_leg+=1
    if cookie[i][heart[1]+1] == "*":
        right_leg+=1

print(left_arm,right_arm,body,left_leg,right_leg)
        
        
        
        
        
    
    
    
        
    