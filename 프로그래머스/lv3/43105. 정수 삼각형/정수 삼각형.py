def solution(triangle):
    length = len(triangle)
    dp = [[0 for _ in range(length)] for _ in range(length)]
    
    for x in range(length):
        if x == 0:
            dp[0][0] = triangle[0][0]
        else:
            dp[x][0] = dp[x-1][0] + triangle[x][0]
            dp[x][x] = dp[x-1][x-1] + triangle[x][x]
            
    for x in range(2, length):
        for y in range(1, len(triangle[x])-1):
            dp[x][y] = max(dp[x-1][y-1], dp[x-1][y]) + triangle[x][y]
            
    # 가장 밑단에 완성된 dp에서 최댓값 리턴
    result = 0
    for y in range(length):
        result = max(result, dp[length-1][y])
        
    return result
            
        