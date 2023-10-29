import heapq

def solution(operations):
    answer = [0, 0]
    min_q = []
    max_q = []
    number_dict = {}
    
    for operation in operations:
        option, number_str = operation.split(" ")
        number = int(number_str)
        # 큐에 주어진 숫자를 삽입
        if option == "I":
            heapq.heappush(min_q, number)
            heapq.heappush(max_q, -1*number)
            if number not in number_dict:
                number_dict[number] = 1
            else:
                number_dict[number] += 1
        # 큐에서 최댓값을 삭제
        elif number == 1:
            while max_q:
                temp_num = heapq.heappop(max_q)
                if number_dict[-1*temp_num] > 0:
                    number_dict[-1*temp_num] -= 1
                    break
        # 큐에서 최솟값을 삭제
        else:
            while min_q:
                temp_num = heapq.heappop(min_q)
                if number_dict[temp_num] > 0:
                    number_dict[temp_num] -= 1
                    break
    # 최대/최소값 찾기
    while min_q:
        temp_num = heapq.heappop(min_q)
        if number_dict[temp_num] > 0:
            answer = [temp_num, temp_num]
            break
    while max_q:
        temp_num = heapq.heappop(max_q)
        if number_dict[-1*temp_num] > 0:
            answer[0] = -1*temp_num
            if answer[1] == 0:
                answer[1] = temp_num
            break
        
    return answer