import sys

N, game = sys.stdin.readline().strip().split()
N = int(N)
find_game_num = 0
if game == "Y":
    find_game_num = 1
elif game == "F":
    find_game_num = 2
elif game == "O":
    find_game_num = 3

people = set()
for i in range(N):
    person = sys.stdin.readline().strip()
    if person not in people:
        people.add(person)

print(len(people) // find_game_num)