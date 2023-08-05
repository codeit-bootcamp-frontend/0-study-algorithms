import sys

def cal_walk(arr):
    line = []
    ans = 0
    for student in arr:
        i = 0
        while i < len(line) and line[i] < student:
            i += 1
        ans += len(line) - i
        line.insert(i, student)
    return ans

P = int(sys.stdin.readline())
for n in range(P):
    arr = list(map(int, sys.stdin.readline().strip().split()[1:]))
    print(n+1, cal_walk(arr))