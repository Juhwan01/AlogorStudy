import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input().rstrip())

ability=[]
min_value = float('inf')

for i in range(n):
    ability.append(list(map(int,input().rstrip().split())))



people = [i for i in range(n)]
teams = list(combinations(people, n//2))
size=len(teams)
for i in range(size//2):
    team_a=teams[i]
    team_b=teams[size-i-1]
    sum_a=0
    sum_b=0
    for j in team_a:
        for k in team_a:
            sum_a+=ability[j][k]
    for j in team_b:
        for k in team_b:
            sum_b+=ability[j][k]
    result = abs(sum_a-sum_b)
    min_value = min(min_value,result)

print(min_value)
