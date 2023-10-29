def solution(phone_book):
    partial_num = {}
    entire_num = {}
    answer = True
    for num in phone_book:
        if num in partial_num:
            return False
        entire_num[num] = True
        
        partial = ""
        for digit in num[:-1]:
            partial += digit    
            if partial in entire_num:
                return False
            partial_num[partial] = True
    
    return answer