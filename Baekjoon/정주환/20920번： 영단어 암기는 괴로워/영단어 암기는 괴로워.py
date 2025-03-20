import sys
input = sys.stdin.readline

my_dict = {}
n,m = map(int,input().split())

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in my_dict :
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    else:
        continue
alpha = sorted(my_dict.items())
length = sorted(alpha, key = lambda x: len(x[0]), reverse = True)
frequency = sorted(length, key = lambda x: x[1], reverse = True)

for key,value in frequency:
    print(key)