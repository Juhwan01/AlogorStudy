import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().rstrip().split()))

add,sub, mul, div = map(int,input().rstrip().split())


min_value=float('inf')
max_value=float('-inf')

def dfs(depth,result,add,sub, mul, div):
    global min_value,max_value
    
    if depth == n:
        min_value = min(result,min_value)
        max_value = max(result,max_value)
        return
    
    if add>0:
        dfs(depth+1,result+numbers[depth],add-1,sub, mul, div)
    if sub>0:
        dfs(depth+1,result-numbers[depth],add,sub-1, mul, div)
    if mul>0:
        dfs(depth+1,result*numbers[depth],add,sub, mul-1, div)
    if div>0:
        if result<0 : 
            dfs(depth+1,-(-result//numbers[depth]),add,sub, mul, div-1)
        else:
            dfs(depth+1,result//numbers[depth],add,sub, mul, div-1)
    
dfs(1, numbers[0], add, sub, mul, div)

print(max_value)
print(min_value)


