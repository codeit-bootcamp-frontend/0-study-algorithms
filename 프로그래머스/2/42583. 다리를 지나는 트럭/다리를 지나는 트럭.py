from collections import deque

def solution(bridge_length, weight, truck_weights):
    second = 0
    allowed_weight = weight
    sum_weight = 0
    waiting_queue = deque()
    going_queue = deque()
    
    for truck in truck_weights:
        waiting_queue.append(truck)
        
    while (waiting_queue or going_queue):
        second += 1
        # 1. 다리에서 빠져나갈 트럭 확인
        if (going_queue and second == going_queue[0][0] + bridge_length):
            exiting_weight = going_queue.popleft()[1]
            sum_weight -= exiting_weight
        
        # 2. 다리에 추가할 트럭 확인
        # 저장 형태: (entered_second, weight)
        if (waiting_queue and waiting_queue[0] + sum_weight <= allowed_weight):
            entering_weight = waiting_queue.popleft()
            going_queue.append((second, entering_weight))
            sum_weight += entering_weight

    return second