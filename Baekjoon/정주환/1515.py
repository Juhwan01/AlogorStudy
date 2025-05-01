import sys
input=sys.stdin.readline
S = input().rstrip()
n = 0
while len(S):
    n+=1
    num = str(n)
    while len(num) and len(S):
        if num[0] == S[0]:
            S=S[1:]
        num=num[1:]
        
print(n)