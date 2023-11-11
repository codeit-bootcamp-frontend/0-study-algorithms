class Node(object):
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0
    
    def listSize(self):
        return self.size
    
    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True
    
    def selectNode(self, idx):
        if idx > self.size:
            print("Overflow: Index Error")
            return None
        if idx == 0:
            return self.head
        if idx == self.size:
            return self.tail
        if idx <= self.size//2:
            target = self.head
            for _ in range(idx):
                target = target.next
            return target
        else:
            target = self.tail
            for _ in range(self.size - idx):
                target = target.prev
            return target
    
    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head = Node(value, None, self.head)
            tmp.prev = self.head
        self.size += 1
            
    
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.tail.prev
            newNode = Node(value, tmp, self.tail)
            tmp.next = newNode
            self.tail.prev = newNode
        self.size += 1
    
    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            if tmp == self.head:
                self.appendleft(value)
            elif tmp == self.tail:
                self.append(value)
            else:
                tmp_prev = tmp.prev
                newNode = Node(value, tmp_prev, tmp)
                tmp_prev.next = newNode
                tmp.prev = newNode
        self.size += 1
        
    def findNode(self, data): #O(n)
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.data == data:
                return crnt_node
            crnt_node = crnt_node.next
        return False
    
    def deleteNode(self, node):
        if node == self.head:
            self.head = node.next
        elif node == self.tail:
            self.tail = self.tail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1
    
    def popleft(self):
        if self.is_empty():
            return
        self.head = self.head.next
        self.size -= 1
    
    def printlist(self):
        target = self.head
        while target != self.tail:
            if target.next != self.tail:
                print(target.data, '<=> ', end='')
            else:
                print(target.data)
            target = target.next

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    cache_dict = {}
    d_list = DList()
    
    for city_before_modify in cities:
        city = city_before_modify.lower()
        # 캐시에 있는지 확인해서 있으면 삭제
        if city in cache_dict:
            answer += 1
            d_list.deleteNode(d_list.findNode(city))
            cache_dict[city] -= 1
            if cache_dict[city] == 0:
                del cache_dict[city]
        else:
            answer += 5
        # 캐시에 추가
        d_list.append(city)
        if city in cache_dict:
            cache_dict[city] += 1
        else:
            cache_dict[city] = 1
        # 길이 확인 후 넘치면 하나 제거
        if d_list.listSize() > cacheSize:
            head_data = d_list.head.data
            cache_dict[head_data] -= 1
            if cache_dict[head_data] == 0:
                del cache_dict[head_data]
            d_list.popleft()
    
    return answer