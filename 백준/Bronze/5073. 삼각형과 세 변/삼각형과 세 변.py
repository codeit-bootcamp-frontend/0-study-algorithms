arr = []
while True:
    input_tri = list(map(int, input().split()))
    if (input_tri == [0, 0, 0]):
        break
    arr.append(sorted(input_tri))

ans = []
for tri in arr:
    if tri[0] + tri[1] <= tri[2]:
        ans.append("Invalid")
        continue
    if tri[0] == tri[1]:
        if tri[1] == tri[2]:
            ans.append("Equilateral")
        else:
            ans.append("Isosceles")
        continue
    if tri[1] == tri[2]:
        if tri[1] == tri[0]:
            ans.append("Equilateral")
        else:
            ans.append("Isosceles")
        continue
    ans.append("Scalene")

for i in ans:
    print(i)