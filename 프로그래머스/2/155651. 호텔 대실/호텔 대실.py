def add_10_minute(t):
    add_m = int(t[2:]) + 10
    if add_m >= 60:
        next_h = int(t[:2]) + 1
        if next_h < 10:
            next_h = "0" + str(next_h)
        else:
            next_h = str(next_h)
        return next_h + "0" + str(add_m - 60)
    return t[:2] + str(add_m)

def solution(book_time):
    start_list = []
    end_list = []
    for book in book_time:
        start_list.append(book[0].replace(":", ""))
        end_list.append(add_10_minute(book[1].replace(":", "")))

    start_list.sort(reverse=True)
    end_list.sort(reverse=True)
    
    answer = 0
    need = 0
    while start_list:
        if end_list[-1] <= start_list[-1]:
            end_list.pop()
            need -=1
        else:
            start_list.pop()
            need += 1
            answer = max(answer, need)
    
    return answer