import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
r,c,d = map(int,input().rstrip().split())
cnt=0
house=[]
flag=False

def find(r,c):
    start_row = 0 if r-4<0 else r-4
    start_col = 0 if c-4<0 else c-4
    end_row = n if r+5>n else r+5
    end_col = m if c+5>m else c+5
    for i in range(start_row,end_row):
        for j in range(start_col,end_col):
            if house[i][j] == 0:
                return True
    return False

for i in range(n):
    house.append(list(map(int,input().rstrip().split())))

while True:
    if house[r][c] == 0:
        house[r][c]=2
        cnt+=1
        
    if find(r,c):
        d = 3 if d-1<0 else d-1
        if d==0:
            r = r-1 if house[r][r-1]==0 else r
        elif d==1:
            c =  c+1 if house[r][c+1]==0 else c
        elif d==2:
            r = r+1 if house[r][r+1]==0 else r
        elif d==3:
            c = c-1 if house[r][c-1]==0 else c
    else:
        if d==0:
            if house[r+1][c]==1:
                break
            else:
                r=r+1
        elif d==1:
            if house[r][c-1]==1:
                break
            else:
                c=c-1
        elif d==2:
            if house[r-1][c]==1:
                break
            else:
                r=r-1
        elif d==3:
            if house[r][c+1]==1:
                break
            else:
                c=c+1

print(cnt)

