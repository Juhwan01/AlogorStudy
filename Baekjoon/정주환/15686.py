import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

street = defaultdict(list)
for i in range(n):
    s = list(map(int,input().rstrip().split()))
    for j in range(n):
        if s[j] == 1:
            street[1].append([i,j])
        elif s[j] == 2:
            street[2].append([i,j])

all_combinations = list(combinations(street[2],m))
min_street = float('inf')
for combo in all_combinations:
    sum=0
    for s in street[1]:
        min_value = float('inf')
        for j in combo:
            min_value = min(min_value,abs(s[0]-j[0])+abs(s[1]-j[1]))
        sum+=min_value
    min_street = min(sum,min_street)


print(min_street)