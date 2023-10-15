def solution(m, n, puddles):
    if m == 1 or n == 1:
        return 1

    map = [[-1 for _ in range(n)] for _ in range(m)]
    for x, y in puddles:
        map[x-1][y-1] = False
        
    is_puddle = False
    for i in range(m):
        if is_puddle or map[i][0] == False:
            map[i][0] = 0
            is_puddle = True
        else:
            map[i][0] = 1
            
    is_puddle = False        
    for i in range(n):
        if is_puddle or map[0][i] == False:
            map[0][i] = 0
            is_puddle = True
        else:
            map[0][i] = 1
            
    for i in range(m-1):
        for j in range(n-1):
            x, y = i+1, j+1
            if map[x][y] == False:
                map[x][y] = 0
            else:
                map[x][y] = (map[x-1][y] + map[x][y-1]) % 1000000007
            
    return map[-1][-1]