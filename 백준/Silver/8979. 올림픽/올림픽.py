import sys

N, K = map(int, sys.stdin.readline().strip().split())


def compare_medal(compare, new):
    compare_gold, compare_silver, compare_bronze = compare[0], compare[1], compare[2]
    new_gold, new_silver, new_bronze = new[0], new[1], new[2]
    if compare_gold == new_gold:
        if compare_silver == new_silver:
            if compare_bronze == new_bronze:
                return "same"
            elif compare_bronze > new_bronze:
                return "compare"
            else:
                return "new"
        elif compare_silver > new_silver:
            return "compare"
        else:
            return "new"
    elif compare_gold > new_gold:
        return "compare"
    else:
        return "new"


rank_arr = []
for _ in range(N):
    new = list(map(int, sys.stdin.readline().strip().split()))
    new.append(1)
    for i in range(len(rank_arr)):
        compare = rank_arr[i]
        compare_result = compare_medal(compare[1:4], new[1:4])
        if compare_result == "compare":
            new[4] += 1
        elif compare_result == "new":
            compare[4] += 1
    rank_arr.append(new)  # num, gold, silver, bronze, rank

rank_arr.sort(key=lambda x: x[0])
print(rank_arr[K-1][4])