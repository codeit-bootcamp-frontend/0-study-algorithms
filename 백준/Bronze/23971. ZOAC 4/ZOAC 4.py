H, W, N, M = map(int, input().split())

num_width = (W + M) // (M + 1)
num_height = (H + N) // (N + 1)
ans = num_width * num_height

print(ans)
