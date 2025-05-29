n, k = map(int, input().split())
line = list(input())
count = 0

for position in range(n):
    if line[position] == 'P':
        left = position - k
        if left < 0:
            left = 0
        right = position + k
        if right >= n:
            right = n - 1

        i = left
        while i <= right:
            if line[i] == 'H':
                line[i] = '-'
                count += 1
                break
            i += 1

print(count)
