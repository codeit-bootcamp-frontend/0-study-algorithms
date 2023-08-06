import sys

word = sys.stdin.readline().strip()
vowel = {'a', 'e', 'i', 'o', 'u'}
while(word != "end"):
    has_vowel = False
    consecutive_vowel, consecutive_consonant = 0, 0
    prev = ""
    is_acceptable = True

    for letter in word:
        if letter == prev:
            if letter != "e" and letter != "o":
                is_acceptable = False
        prev = letter

        if letter in vowel:
            has_vowel = True
            consecutive_vowel += 1
            consecutive_consonant = 0
        else:
            consecutive_vowel = 0
            consecutive_consonant += 1
        if consecutive_vowel == 3 or consecutive_consonant == 3:
            is_acceptable = False

        if not is_acceptable:
            break
    if is_acceptable and has_vowel:
        print("<{}> is acceptable.".format(word))
    else:
        print("<{}> is not acceptable.".format(word))

    word = sys.stdin.readline().strip()

