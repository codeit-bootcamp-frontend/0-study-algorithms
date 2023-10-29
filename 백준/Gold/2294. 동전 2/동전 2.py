import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().strip()))
coins = list(set(coins))
coins.sort(reverse=True)

visited = set()
queue = deque()


def cal_min_coins():
    for coin in coins:
        queue.append((coin, 1))
        visited.add(coin)

    while queue:
        value, cnt = queue.popleft()
        if value == k:
            print(cnt)
            return
        for coin in coins:
            if coin + value <= k and coin + value not in visited:
                visited.add(coin + value)
                queue.append((coin + value, cnt + 1))
    print(-1)


cal_min_coins()
