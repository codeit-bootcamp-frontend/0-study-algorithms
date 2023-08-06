import sys

def toggle_switch(n):
    if n == 1:
        return 0
    else:
        return 1

switch_num = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().strip().split()))

student_num = int(sys.stdin.readline())
for i in range(student_num):
    student = list(map(int, sys.stdin.readline().strip().split()))
    student_sex, student_get_num = student[0], student[1]
    if student_sex == 1:
        compare_num = student_get_num
        while compare_num <= len(switch):
            switch[compare_num-1] = toggle_switch(switch[compare_num-1])
            compare_num += student_get_num
    elif student_sex == 2:
        switch[student_get_num-1] = toggle_switch(switch[student_get_num-1])
        moving = 1
        while student_get_num - moving >= 1 and student_get_num + moving <= len(switch):
            if switch[student_get_num - moving - 1] == switch[student_get_num + moving - 1]:
                switch[student_get_num - moving - 1] = toggle_switch(switch[student_get_num - moving - 1])
                switch[student_get_num + moving - 1] = toggle_switch(switch[student_get_num + moving - 1])
            else:
                break
            moving += 1

line_idx = 1
for i in switch[:-1]:
    if line_idx == 20:
        print(i)
        line_idx = 1
    else:
        print(i, end=" ")
        line_idx += 1
print(switch[-1])

