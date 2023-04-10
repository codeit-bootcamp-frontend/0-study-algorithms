import sys
input = sys.stdin.readline
K = int(input())
arr = []
for _ in range(K):
    number = int(input())
    if number == 0:
        arr.pop()
        continue
    arr.append(number)
print(sum(arr))
