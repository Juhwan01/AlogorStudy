import heapq
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
results = []

for _ in range(n):
    numbers.append(int(input()))

left = []  
right = []  

for i in range(n):
    num = numbers[i]
    
    if len(left) == 0:
        heapq.heappush(left, -num)
    else:
        if num <= -left[0]:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)
    
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))
    
    results.append(-left[0])

for result in results:
    print(result)
