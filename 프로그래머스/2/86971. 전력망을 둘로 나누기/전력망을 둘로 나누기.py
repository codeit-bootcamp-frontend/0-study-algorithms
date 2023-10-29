from collections import deque


def solution(n, wires):
    def bfs(graph, node):
        node_num = 0
        visited = {}
        queue = deque()
        queue.append(node)
        while queue:
            curr_node = queue.popleft()
            if curr_node in visited:
                break
            node_num += 1
            visited[curr_node] = True
            for next_node in graph[curr_node]:
                if next_node not in visited:
                    queue.append(next_node)
        return node_num
    
    answer = 99999
    graph = {}
    
    for left, right in wires:
        if left not in graph:
            graph[left] = [right]
        else:
            graph[left].append(right)
        if right not in graph:
            graph[right] = [left]
        else:
            graph[right].append(left)

    for i in range(len(wires)):
        new_graph = graph
        new_graph[wires[i][0]].remove(wires[i][1])
        new_graph[wires[i][1]].remove(wires[i][0])
        left = bfs(new_graph, wires[i][0])
        right = bfs(new_graph, wires[i][1])
        new_graph[wires[i][0]].append(wires[i][1])
        new_graph[wires[i][1]].append(wires[i][0])
        distract = left - right
        if distract < 0:
            distract *= (-1)
        answer = min(answer, distract)
            
    return answer