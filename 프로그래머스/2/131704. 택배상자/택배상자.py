def solution(order):
    answer = 0
    assist_container = []
    order_idx = 0
    for i in range(len(order)):
        box_num = i + 1
        # 보조 컨테이너 박스에서 일치하는 만큼 실어주기
        while assist_container and assist_container[-1] == order[order_idx]:
            answer += 1
            order_idx += 1
            assist_container.pop()
        # 컨테이너 박스와 필요 박스가 일치할 때
        if box_num == order[order_idx]:
            answer += 1
            order_idx += 1
        # 둘 다 일치하지 않을 때
        else:
            if box_num < order[order_idx]:
                assist_container.append(box_num)
            else:
                break
    
    # 보조 컨테이너 한 번 더 확인
    while (assist_container and assist_container[-1] == order[order_idx]):
        answer += 1
        order_idx += 1
        assist_container.pop()
        
    return answer