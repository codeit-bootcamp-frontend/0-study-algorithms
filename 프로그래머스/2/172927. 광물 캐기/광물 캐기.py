def add_tired(weapon, mineral):
    if weapon == 0:
        return 1
    elif weapon == 1:
        if mineral == 1:
            return 5
        else:
            return 1
    else:
        if mineral == 1:
            return 25
        elif mineral == 2:
            return 5
        else:
            return 1

def solution(picks, minerals):
    minerals_sort_list = []
    answer = 0
    minerals = minerals[:(sum(picks)*5)]
    length = len(minerals)
    for i in range((length -1) // 5 + 1):
        dia, iron, stone = 0, 0, 0
        if i == (length -1) // 5:
            for mineral in minerals[5*i:]:
                if mineral == "diamond":
                    dia += 1
                elif mineral == "iron":
                    iron += 1
                else:
                    stone += 1
        else:
            for mineral in minerals[5*i:5*i+5]:
                if mineral == "diamond":
                    dia += 1
                elif mineral == "iron":
                    iron += 1
                else:
                    stone += 1
        minerals_sort_list.append((i, dia, iron, stone))
    minerals_sort_list.sort(reverse=True, key=lambda x: (x[1], x[2], x[3]))
    
    minerals_idx = 0
    weapon_idx = 0
    while True:
        if picks[weapon_idx] != 0:
            break
        else:
            weapon_idx += 1
    
    while weapon_idx <= 2 and minerals_idx < len(minerals_sort_list):
        if picks[weapon_idx] == 0:
            wepon_idx += 1
            continue

        picks[weapon_idx] -= 1
        for i in range(1, 4):
            for _ in range(minerals_sort_list[minerals_idx][i]):
                answer += add_tired(weapon_idx, i)
            
        if picks[weapon_idx] == 0:
            weapon_idx += 1
        minerals_idx += 1
    
    return answer