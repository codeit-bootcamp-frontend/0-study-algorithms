def solution(n):
    memo = [1, 1]
    
    # memoization
    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    
    return memo[n] % 1234567