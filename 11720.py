while True:
    n1 = int(input())
    if 1 <= n1 <= 100:
        break
    print("1 ~ 100")
n2 = input()
total = 0 
for i in range(n1):
    total += int(n2[i])
print(total)
    