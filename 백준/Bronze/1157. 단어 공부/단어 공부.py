word = input().upper()
arr = [i for i in word]
dic = {}
for letter in arr:
    if letter not in dic:
        dic[letter] = 1
    else:
        dic[letter] += 1

max_count = 0
ans = ""
for i in dic:
    if dic[i] > max_count:
        max_count = dic[i]
        ans = i
    elif dic[i] == max_count:
        ans = "?"


print(ans)