import sys
input = sys.stdin.readline

n, game = input().split()
n = int(n)
members = []

for i in range(n):
        name = input().rstrip()
        members.append(name)
            
member_cnt = len(set(members))

if game == "Y":
    print(member_cnt)
elif game == "F":
    print(member_cnt//2)
elif game == "O":
    print(member_cnt//3)