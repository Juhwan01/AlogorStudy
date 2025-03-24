import sys
input = sys.stdin.readline

sum=0
h,w = map(int,input().split())
height = list(map(int,input().split()))
container = [[0 for _ in range(h)]for _ in range(w)]

for i in range(w):
    for j in range(height[i]):
        container[i][j] = 1
        
for i in range(h):
    cnt=0
    j=0
    flag=False
    while(j<w):
        if container[j][i] == 1:
            flag = not flag
            if not flag:
                j-=1
                sum+=cnt
                cnt=0
        elif container[j][i] == 0 and flag:
            cnt+=1
        j+=1
print(sum)
        
