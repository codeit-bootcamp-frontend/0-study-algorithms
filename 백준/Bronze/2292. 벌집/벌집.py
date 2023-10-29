N = int(input())
ans = 1
bound = 1
while (N > 1 and N > bound):
    bound += 6*ans
    ans += 1

print(ans)