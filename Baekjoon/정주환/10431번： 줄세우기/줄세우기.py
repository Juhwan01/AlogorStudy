import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
members = defaultdict(int)

for i in range(1,t+1):
    member_list = list(map(int, input().split()))[1:]
    cnt =0
    for j in range (20):
        for k in range(j):
            if member_list[j] < member_list[k]:
                value = member_list.pop(j)
                member_list.insert(k, value)
                cnt+=j-k
                break
    print(i, cnt)
        