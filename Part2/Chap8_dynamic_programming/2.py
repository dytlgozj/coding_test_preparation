# 아주 대표적인 DP 문제이다. 점화식을 a[i] = min(a[i / 2], a[i / 3], a[i / 5], a[i - 1]) + 1 로 세울 수 있어야
# 풀 수 있는 문제였다.

x = int(input())
dp = [0] * 30001

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[x])
