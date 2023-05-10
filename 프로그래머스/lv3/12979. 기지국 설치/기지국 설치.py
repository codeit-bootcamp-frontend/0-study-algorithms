import math

def solution(n, stations, w):
    answer = 0
    bandwidth = 2*w + 1

    network_areas = []
    for s in stations:
        left = s - w
        right = min(s + w, n)
        network_areas.append((left, right))
        
    print(network_areas)
        
    start = 1
    for left, right in network_areas:
        if start < left:
            answer += math.ceil((left-start) / bandwidth)
        start = right + 1
        
    if start <= n:
        answer += math.ceil((n-start+1) / bandwidth)
        
    return answer