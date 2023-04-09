def mergeSort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr) + 1)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    merged = []
    lp, rp = 0, 0

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            merged.append(left[lp])
            results.append(left[lp])
            lp += 1
        else:
            merged.append(right[rp])
            results.append(right[rp])
            rp += 1

    while lp < len(left):
        merged.append(left[lp])
        results.append(left[lp])
        lp += 1

    while rp < len(right):
        merged.append(right[rp])
        results.append(right[rp])
        rp += 1

    return merged


n, k = map(int, input().split())
arr = list(map(int, input().split()))

results = []
mergeSort(arr)

if len(results) >= k:
    print(results[k-1])
else:
    print(-1)
