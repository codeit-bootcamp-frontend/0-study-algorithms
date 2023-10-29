def solution(n, costs):
    # 가중치가 작은 것부터 택하되, 사이클은 아니도록
    # => 크루스칼 알고리즘
    answer = 0
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    for cost in costs:
        start_parent_node = parent[cost[0]]
        end_parent_node = parent[cost[1]]
        if start_parent_node == end_parent_node:
            continue
        elif start_parent_node < end_parent_node:
            for i in range(n):
                if parent[i] == end_parent_node:
                    parent[i] = start_parent_node
        else:
            for i in range(n):
                if parent[i] == start_parent_node:
                    parent[i] = end_parent_node

        answer += cost[2]
        if sum(parent) == 0:
            return answer
    return answer