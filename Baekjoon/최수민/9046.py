import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    s=input().rstrip('\n').replace(' ','')
    d={}
    for c in s:
        d[c] = d.get(c, 0) + 1
    if not d:
        print('?')
        continue
    m = max(d.values())
    k = [x for x in d if d[x] == m]
    print(k[0] if len(k) == 1 else '?')
