import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
todo_list = []
cal = []

for _ in range(N):
    a = list(map(int, input().split()))
    todo_list.append(a)

for todo in todo_list:
    for i in range(todo[0], todo[1]+1):
        cal.append(i)

counter = Counter(cal)
duplicates = [num for num, count in counter.items() if count > 1]
cnt = []
for d in duplicates:
    cnt.append(cal.count(d))
connected_segments = []

new_cal = sorted(set(cal))

temp = [new_cal[0]]
for i in range(1, len(new_cal)):
    if new_cal[i] == new_cal[i - 1] + 1:
        temp.append(new_cal[i])
    else:
        connected_segments.append(temp)
        temp = [new_cal[i]]
connected_segments.append(temp)
wh = []
for cs in connected_segments:
    h = 1
    for i in range (len(duplicates)):
        if duplicates[i] in cs:
            if h < cnt[i]:
                h = cnt[i]
    wh.append(h*len(cs))
    
print(sum(wh))