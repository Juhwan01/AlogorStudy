import sys
input = sys.stdin.readline

x = []

for _ in range(9):
    a = int(input())
    x.append(a)
    
x.sort()

total = sum(x)
found = False

for i in range(8):
    if found:
        break
    for j in range(i+1, 9):
        if total - x[i] - x[j] == 100:
            a, b = x[i], x[j]
            found = True
            break
        
for i in x:
    if i != a and i != b:
        print(i)
            
            
        
    
    
    
    
    