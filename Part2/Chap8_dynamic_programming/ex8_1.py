# Top-Down 방식. 재귀. (Memoization) DP.

dp = [0] * 101

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if dp[x] != 0:
        return dp[x]
    else:
        dp[x] = fibo(x - 1) + fibo(x - 2)
        return dp[x]

print(fibo(100))


# Bottom-Up 방식. 반복문.

dp = [0] * 101

def fibo(x):
    dp[1] = 1
    dp[2] = 1

    for i in range(3, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[x]

print(fibo(100))
