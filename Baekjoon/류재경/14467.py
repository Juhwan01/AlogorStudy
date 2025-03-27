import sys
input = sys.stdin.readline

n = int(input())

cow_position = {}  
cross_count = 0

for _ in range(n):
    
    cow_id, position = map(int, input().split())
    
    if cow_id in cow_position:
       
        if cow_position[cow_id] != position:
            cross_count += 1
    
    cow_position[cow_id] = position

print(cross_count)