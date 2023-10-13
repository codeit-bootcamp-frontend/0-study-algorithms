def solution(nums):
    dict = {}
    num_pocketmon = len(nums)
    num_kind_pocketmon = 0
    for num in nums:
        if num not in dict:
            dict[num]  = True
            num_kind_pocketmon += 1
            
    return min(num_kind_pocketmon, num_pocketmon // 2)