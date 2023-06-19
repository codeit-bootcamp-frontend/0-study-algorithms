def getMinDist(dp1, dp2):
    # 1. None인 경우
    if dp1 == None:
        if dp2 == None:
            return None
        else:
            return (dp2[0]+1, dp2[1]%1000000007)
    elif dp2 == None:
        return (dp1[0]+1, dp1[1]%1000000007)
    # 2. 거리가 왼/위 동일한 경우
    elif dp1[0] == dp2[0]:
        return (dp1[0]+1, (dp1[1] + dp2[1])%1000000007)
    # 3. 거리가 왼쪽이 더 짧은 경우
    elif dp1[0] < dp2[0]:
        return (dp1[0]+1, dp1[1]%1000000007)
    # 4. 거리가 위가 더 짧은 경우
    else:
        return (dp2[0]+1, dp2[1]%1000000007)
       

def solution(m, n, puddles):
    map_info = [[1 for _ in range(m)] for _ in range(n)]
    
    # 물이 잠긴 지역은 0
    if puddles[0]:
        for y, x in puddles:
            map_info[x-1][y-1] = 0
        
    dp = [[None for _ in range(m)] for _ in range(n)]
    dp[0][0] = (0, 1)  # [0]: 최단거리 [1]: 최단거리 경우의 수
    
    # 오른쪽, 아래 직선 dp
    for x in range(1, n):
        if map_info[x][0] == 1 and dp[x-1][0]:
            dp[x][0] = (dp[x-1][0][0] + 1, 1)
    
    for y in range(1, m):
        if map_info[0][y] == 1 and dp[0][y-1]:
            dp[0][y] = (dp[0][y-1][0] + 1, 1)
            
    # 이외 dp
    for x in range(1, n):
        for y in range(1, m):
            if map_info[x][y] == 1:
                dp[x][y] = getMinDist(dp[x-1][y], dp[x][y-1])
                
                
    if not dp[n-1][m-1]:
        return 0
    return dp[n-1][m-1][1]
            