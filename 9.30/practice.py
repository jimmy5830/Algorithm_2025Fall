
dp = [0]*100
dp[0] = 1
dp[1] = 1

def fib(n):

    if dp[n] == 0:
        dp[n] = fib(n-1) + fib(n-2)

    return dp[n]

print(fib(10))