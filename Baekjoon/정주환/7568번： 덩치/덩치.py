import sys
input = sys.stdin.readline

n = int(input())
people = []
for i in range(n):
    height, weight = map(int, input().split())
    people.append((height, weight))

rank = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt +=1
    rank.append(cnt)

print(' '.join(map(str, rank)))