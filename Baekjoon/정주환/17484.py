import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

fuel = float('inf')

need_fuel = []
for _ in range(N):
    need_fuel.append(list(map(int,input().rstrip().split())))

def dfs(depth,result,direction,index):
    global fuel
    
    if depth == N:
        fuel = min(result,fuel)
        return
    
    if direction==-1:
        dfs(depth+1,result+need_fuel[depth][index],0,index)
        if index+1<M:
            dfs(depth+1,result+need_fuel[depth][index+1],1,index+1)
    if direction==0:
        if index+1<M:
            dfs(depth+1,result+need_fuel[depth][index+1],1,index+1)
        if index-1>=0:
            dfs(depth+1,result+need_fuel[depth][index-1],-1,index-1)
    if direction==1:
        dfs(depth+1,result+need_fuel[depth][index],0,index)
        if index-1>=0:
            dfs(depth+1,result+need_fuel[depth][index-1],-1,index-1)
    if direction==2:
        if index+1<M:
            dfs(depth+1,result+need_fuel[depth][index+1],1,index+1)
        if index-1>=0:
            dfs(depth+1,result+need_fuel[depth][index-1],-1,index-1)
        dfs(depth+1,result+need_fuel[depth][index],0,index)
    

for i in range(M):
    dfs(1, need_fuel[0][i], 2, i)

print(fuel)