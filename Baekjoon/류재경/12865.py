N, K = map(int, input().split())
a = []

for i in range(N):
    W, V = map(int, input().split())
    a.append([W,V])

dp = [0] * (K + 1)

for w, v in a:
    for i in range(K, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)
        
print(dp[K])