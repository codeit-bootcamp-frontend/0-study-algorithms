def solution(n, money):
    dp = [1] + [0] * n
    # money의 종류를 돌면서 현재 선택된 동전(coin)으로 n원 이하까지의 금액(price)을 만들 수 있는 경우의 수를 dp에 넣는다.
    # price를 만드는 경우의 수는 coin을 한 번 써서 price-coin을 만드는 수와 같다.
    # => dp[price] += dp[price - coin]
    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                dp[price] += dp[price - coin]
    
    return dp[n] % 1000000007