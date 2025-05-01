import sys
input = sys.stdin.readline
t=0
cur_pos = [0,0]

N = int(input())

apple_map = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())

for _ in range(K):
    i,j = map(int,input().rstrip().split())
    apple_map[i][j] = 1
    
L = int(input())

for _ in range(L):
    x,c = map(str,input().rstrip().split())
    x = int(x)

 
    