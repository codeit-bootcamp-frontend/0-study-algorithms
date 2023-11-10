def solution(want, number, discount):
    answer = 0
    # 구매 idx dict 및 구매 list 생성
    purchase_idx_dict = {}
    for i, w in enumerate(want):
        purchase_idx_dict[w] = i
    purchase_list = [0 for _ in range(len(want))]
    
    def check_exactly_purchase(pur_list, want_list):
        for i in range(len(want_list)):
            if not pur_list[i] == want_list[i]:
                return False
        return True
    
    # 초기 구매 확인
    for d in range(10):
        if discount[d] in purchase_idx_dict:
            purchase_list[purchase_idx_dict[discount[d]]] += 1
    if check_exactly_purchase(purchase_list, number):
        answer += 1
    # 하루씩 추가 반영하며 확인
    for d in range(10, len(discount)):
        # 전날 제외
        if discount[d-10] in purchase_idx_dict:
            purchase_list[purchase_idx_dict[discount[d-10]]] -= 1
        # 다음날 추가
        if discount[d] in purchase_idx_dict:
            purchase_list[purchase_idx_dict[discount[d]]] += 1
        # want 비교
        if check_exactly_purchase(purchase_list, number):
            answer += 1
    
    return answer