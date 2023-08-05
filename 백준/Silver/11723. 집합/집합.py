import sys

class Cal_Set:
    def __init__(self):
        self.set = set()
    def add(self, x):
        if x not in self.set:
            self.set.add(x)
    def remove(self, x):
        if x in self.set:
            self.set.remove(x)
    def check(self, x):
        if x in self.set:
            print(1)
            return
        else:
            print(0)
            return
    def toggle(self, x):
        if x in self.set:
            self.set.remove(x)
        else:
            self.set.add(x)
    def all(self):
        self.set = set()
        for i in range(20):
            self.set.add(i+1)
    def empty(self):
        self.set = set()




M = int(sys.stdin.readline())
set1 = Cal_Set()

for _ in range(M):
    command = sys.stdin.readline().strip().split()
    if command[0] == "add":
        set1.add(int(command[1]))
    elif command[0] == "remove":
        set1.remove(int(command[1]))
    elif command[0] == "check":
        set1.check(int(command[1]))
    elif command[0] == "toggle":
        set1.toggle(int(command[1]))
    elif command[0] == "all":
        set1.all()
    elif command[0] == "empty":
        set1.empty()