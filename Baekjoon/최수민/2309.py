a = [int(input()) for _ in range(9)]

total = sum(a)

found = False
for i in range(9):
    for j in range(i+1, 9):
        if total - (a[i] + a[j]) == 100:
            fake1, fake2 = a[i], a[j]
            found = True
            break
    if found:
        break

a.remove(fake1)
a.remove(fake2)
a.sort()
for i in a:
    print(i)