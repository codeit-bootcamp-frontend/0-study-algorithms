def solution(s):
    num_openned = 0
    for str in s:
        if str == ")":
            if num_openned == 0:
                return False
            else:
                num_openned -= 1
        else:
            num_openned += 1

    return (num_openned == 0)