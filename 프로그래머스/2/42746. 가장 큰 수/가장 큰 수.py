def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    if numbers[0] == "0":
        return "0"
    for s in numbers:
        answer += s
    
    return answer
#     def merge_sort(array):
#         if len(array) < 2:
#             return array
#         mid = len(array) // 2
#         low_arr = merge_sort(array[:mid])
#         high_arr = merge_sort(array[mid:])

#         merged_arr = []
#         l = h = 0
#         while l < len(low_arr) and h < len(high_arr):
#             if compare(str(low_arr[l]), str(high_arr[h])): # low_arr[l] < high_arr[h]:
#                 merged_arr.append(low_arr[l])
#                 l += 1
#             else:
#                 merged_arr.append(high_arr[h])
#                 h += 1
#         merged_arr += low_arr[l:]
#         merged_arr += high_arr[h:]
#         return merged_arr        
    
#     def compare_digit(d1, d2):
#         if d1 > d2:
#             return "left"
#         elif d1 < d2:
#             return "right"
#         else:
#             return "same"
    
#     def compare(str1, str2):
#         result_compare_digit = compare_digit(str1[0], str2[0])
#         if result_compare_digit == "left":
#             return True
#         elif result_compare_digit == "right":
#             return False
#         else:
#             if len(str1) == 1 and len(str2) == 1:
#                 return True
#             elif len(str1) == 1:
#                 return compare(str1, str2[1:])
#             elif len(str2) == 1:
#                 return compare(str1[1:], str2)
#             else:
#                 return compare(str1[1:], str2[1:])

#     answer = ''
#     sort_numbers = merge_sort(numbers)
        
#     if sort_numbers[0] == 0:
#         return "0"
#     for n in sort_numbers:
#         answer += str(n)
    