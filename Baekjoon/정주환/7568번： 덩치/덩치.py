# import sys
# input = sys.stdin.readline

# member = {}
# rank = {}
# n = int(input())
# for i in range(n):
#     height, width = map(int, input().split())
#     for mem in member.items():
#         if mem[1][0] < width and mem[1][1] < height:
#             rank[i]=rank.get(mem[0])
#             rank[mem[0]]=rank.get(mem[0])+1
#         else:
#             rank[i]=rank.get(mem[0])
#     if not rank.get(i):
#         rank[i]=i+1
#     member[i] = (width, height)
    
# for mem in rank.items():
#     print(mem[1], end=' ')
    
import sys
input = sys.stdin.readline

    