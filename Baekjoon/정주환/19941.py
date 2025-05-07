import sys
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int,input().strip().split())

string = input()
events=defaultdict(list)

for i in range(len(string)):
    if string[i] == "P":
        events["P"].append(i)
    else:
        events["H"].append(i)

print(events)
            