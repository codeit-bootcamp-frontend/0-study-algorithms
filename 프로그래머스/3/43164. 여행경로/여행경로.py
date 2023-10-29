from copy import deepcopy

def solution(tickets):
    answer = []
    length = len(tickets)
    tickets.sort(key=lambda x: (x[0], x[1]))
    # 항공권 사전 분석
    tickets_idx_dict = {}
    present = ""
    for i, ticket in enumerate(tickets):
        if ticket[0] != present:
            if i > 0:
                tickets_idx_dict[present].append(i-1)
            present = ticket[0]
            tickets_idx_dict[ticket[0]] = [i]
    tickets_idx_dict[present].append(length - 1)
    print(tickets_idx_dict)
    
    def dfs(start, paths, used_tickets):
        if len(paths) == length + 1:
            return paths
        if start in tickets_idx_dict:
            s_idx, e_idx = tickets_idx_dict[start][0], tickets_idx_dict[start][1]
            for next_idx in range(s_idx, e_idx+1):
                if not used_tickets[next_idx]:
                    next_paths = deepcopy(paths)
                    next_paths.append(tickets[next_idx][1])
                    next_used_tickets = deepcopy(used_tickets)
                    next_used_tickets[next_idx] = True
                    result = dfs(tickets[next_idx][1], next_paths, next_used_tickets)
                    if result:
                        return result
        
    return dfs("ICN", ["ICN"], [False for _ in range(length)])
