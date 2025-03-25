import sys
input = sys.stdin.readline

valid = False
n = int(input())
for i in range(n):
    result = []
    problem = input().strip()
    contain = int(input())
    for alpha in problem:
        if problem.count(alpha) >= contain and alpha not in result:
            result.append(alpha)
    print(result)
                
            
