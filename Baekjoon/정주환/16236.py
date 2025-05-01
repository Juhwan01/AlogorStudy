import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

fish_tank = defaultdict(list)

for i in range(n):
    tank = list(map(int,input().rstrip().split()))
    for j in range(n):
        if tank[j] != 0:
            fish_tank[tank[j]].append([i,j])
            
print(fish_tank)