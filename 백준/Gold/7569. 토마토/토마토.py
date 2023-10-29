import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().strip().split())
tomatos = []

for h in range(H):
    tomatos.append([])
    for n in range(N):
        tomatos[h].append(list(map(int, sys.stdin.readline().strip().split())))

visited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatos[h][n][m] == 1:
                queue.append((h, n, m))
                visited[h][n][m] = 0

dm = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

while queue:
    cur_h, cur_n, cur_m = queue.popleft()
    cur_day = visited[cur_h][cur_n][cur_m]
    for i in range(6):
        next_h = cur_h + dh[i]
        next_n = cur_n + dn[i]
        next_m = cur_m + dm[i]
        if 0 <= next_h < H and 0 <= next_n < N and 0 <= next_m < M:
            if tomatos[next_h][next_n][next_m] == 0 and visited[next_h][next_n][next_m] == -1:
                queue.append((next_h, next_n, next_m))
                visited[next_h][next_n][next_m] = cur_day + 1

total_ripped_day = 0
all_ripped = True
for h in range(H):
    for n in range(N):
        for m in range(M):
            if (visited[h][n][m] == -1 and tomatos[h][n][m] == 0):
                all_ripped = False
                break
            total_ripped_day = max(total_ripped_day, visited[h][n][m])
        if not all_ripped:
            break
    if not all_ripped:
        break

if not all_ripped:
    print(-1)
else:
    print(total_ripped_day)