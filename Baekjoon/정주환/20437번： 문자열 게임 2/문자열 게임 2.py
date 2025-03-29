from collections import defaultdict
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    string = input().rstrip()
    n = int(input())
    word = defaultdict(list)
    for i in range(len(string)):
        if string.count(string[i]) >= n:
            word[string[i]].append(i)
    if len(word) == 0:
        print(-1)
    else:
        min_value = float('inf')
        max_value = float('-inf')
        for index in word:
            word_index=word[index]
            for i in range(len(word_index)):
                try:
                    length = word_index[i+n-1] - word_index[i]
                    min_value = min(min_value, length)
                    max_value = max(max_value, length)
                except:
                    continue
        print(min_value+1, max_value+1)