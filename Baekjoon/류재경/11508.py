N = int(input())
x = []
for i in range(N):
    a = int(input())
    x.append(a)
    
x.sort(reverse=True)
C = sum(x)

for i in range(N):
    if (i + 1) % 3 == 0:
        C = C - x[i]

print(C)    