n = int(input())
cow = [-1] * 11  

move_count = 0

for _ in range(n):
    a, b = map(int, input().split())

    if cow[a] == -1:
        cow[a] = b
    else:
        if cow[a] != b:
            move_count += 1
            cow[a] = b 

print(move_count)
