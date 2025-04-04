import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
states = defaultdict(list)
result = {}


for i in range(n):
    data = list(map(int, input().split()))
    states[data[0]] = data[1:]

for key,state in states.items():
    cnt = 1
    for compare in states.values():
        if state[0]<compare[0]:
            cnt+=1
        elif state[0]==compare[0] and state[1]<compare[1]:
            cnt+=1
        elif state[0]==compare[0] and state[1]==compare[1] and state[2]<compare[2]:
            cnt+=1
    result[key] = cnt
print(result.get(k))
