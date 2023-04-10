# 실버 3

# n개의 걸그룹, m개의 퀴즈
# 그룹명, 인원수, 멤버이름
# 팀이름은 0, 멤버이름 1

n, m = map(int, input().split())
team = {}
output = []
# 딕셔너리?
for _ in range(n):
    key = input().strip()
    mem_num = int(input())
    val = []
    for i in range(mem_num):
        val.append(input().strip())
    val.sort()
    team[key] = val

for _ in range(m):
    quize = input().strip()
    type = int(input())
    if type == 1:
        # team2 = {v: k for k, v in team.items()}  # 키 : value 뒤집기
        for k in team:
            if quize in team[k]:
                output.append(k)
    else:
        for data in team[quize]:
            output.append(data)


print(*output, sep="\n")  # 한줄씩 출력 외우기.
