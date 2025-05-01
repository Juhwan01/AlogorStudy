import sys
input = sys.stdin.readline

t = int(input())

events = []
cnt = 0

for _ in range(t):
    start, end = map(int, input().split())
    events.append((start, end))

sorted_events = sorted(events, key=lambda x: (x[1], x[0]))

end_time = 0
for event in sorted_events:
    if end_time <= event[0]:
        cnt += 1
        end_time = event[1]
print(cnt)
