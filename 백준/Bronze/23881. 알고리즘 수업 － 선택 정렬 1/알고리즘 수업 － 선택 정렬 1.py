import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0

for i in range(n - 1, 0, -1):
    index = l.index(max(l[:i + 1]))

    if index != i:
        l[index], l[i] = l[i], l[index]
        cnt += 1

        if cnt == k:
            print(l[index], l[i])
            exit()

print(-1)