import sys
input = sys.stdin.readline

t = int(input())
events = []

for _ in range(t):
    n, m = map(int, input().split())
    events.append((n, 1))
    events.append((m, -1))

events.sort()

cur_mos=0
max_cnt=0
result_strat=[]
result_end=[]
result=[]
flag=False

for time,event in events:
    cur_mos += event
    if cur_mos > max_cnt:
        flag=True
        max_cnt = cur_mos
        result_strat.clear()
        result_end.clear()
        result_strat.append(time)
    elif cur_mos == max_cnt:
        flag=True
        result_strat.append(time)
    elif cur_mos < max_cnt and flag:
        result_end.append(time)
        flag=False

for i in range(len(result_strat)):
    try: 
        if result_end[i]!=result_strat[i+1]:
            result.append(result_strat[0])
            result.append(result_end[i])
            break
    except:
        result.append(result_strat[0])
        result.append(result_end[-1])
print(max_cnt)
print(*result, end=' ')