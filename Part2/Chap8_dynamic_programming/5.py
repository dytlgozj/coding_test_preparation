n, m = map(int, input().split())
coins = []
dp = [10001] * (m + 1)

for _ in range(n):
    coins.append(int(input()))

coins.sort()

dp[0] = 0

for i in range(m + 1):
    if dp[i] != 10001:
        for coin in coins:
            if i + coin <= m:
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
