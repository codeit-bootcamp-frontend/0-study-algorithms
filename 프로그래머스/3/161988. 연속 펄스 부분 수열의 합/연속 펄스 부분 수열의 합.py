def solution(sequence):
    first_plus_max = 0
    first_minus_max = 0
    answer = 0
    for i, n in enumerate(sequence):
        if i % 2 == 0:
            first_plus_max = max(first_plus_max+n, n)
            first_minus_max = max(first_minus_max-n, -n)
        else:
            first_plus_max = max(first_plus_max-n, -n)
            first_minus_max = max(first_minus_max+n, n)
        answer = max(answer, first_plus_max, first_minus_max)
    return answer