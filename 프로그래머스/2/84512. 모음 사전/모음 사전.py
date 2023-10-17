def solution(word):
    made_word = "A"
    answer = 1
    
    while True:
        if made_word == word:
            return answer
        # 다음 단어 만들기
        answer += 1
        if len(made_word) != 5:
            made_word += "A"
        else:
            is_repeat = True
            while is_repeat:
                is_repeat = False
                last_letter = made_word[-1]
                if last_letter == "A":
                    made_word = made_word[:-1] + "E"
                elif last_letter == "E":
                    made_word = made_word[:-1] + "I"
                elif last_letter == "I":
                    made_word = made_word[:-1] + "O"
                elif last_letter == "O":
                    made_word = made_word[:-1] + "U"
                else:
                    is_repeat = True
                    made_word = made_word[:-1]
    
    return answer