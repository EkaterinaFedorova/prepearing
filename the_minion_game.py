# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


# Using KMP algorithm to find substrings in a string
#
VOWELS = "AEIOU"
PLAYER1 = 'Kevin'
PLAYER2 = 'Stuart'


def get_prefix_table(pattern):
    table = [0]
    pattern_length = len(pattern)
    for i in range(1, pattern_length):
        j = 0
        while j < pattern_length and j > 0:
            if pattern[i] == pattern[j]:
                j += 1
        table.append(j)
    return table


def substring_index(needle, haystack, prefixes):
    haystack_length = len(haystack)
    j = 0
    for i in range(haystack_length):
        while j > 0 and needle[j] != haystack[i]:
            j = prefix_table[j - 1]
        if needle[j] == haystack[i]:
            j += 1
            if len(needle) == j:
                yield i - (j - 1)
                i = i - (j - 1) + 1
                j = prefixes[j - 1]
    return None


# input_word = "EQQAEAOQYEQEYYOEEQQYAOEEAQEEOOEYAYOEYAYAEOQYAAYAOYYOQAAYEQAOOAQEAEYAOEEQYYEEAOAOAEQOEYOAOEYOOAAOQEOYEAYYOEAOAQEYYEOQEEEYAOOAYOOAQAEOYOYAEOYQEEEOOQOEAOAAQAOQEYOQEAEAEOOOOQOYQOEQQYEEEYEEOQYYYOEQOQEYAYQQOYEEOAEQOEEEEAAEEYAAQAAQAAYOEAQAQYEYYYEAOYOQEQOOEQOYAYAEEYQAYYQYYAEAYOEYEAOQQQOYYYOYYOYYQYAOEOAOAOYEAAOEOEAEYQAEAQOEOYEEAQOAOQEYOEQOAQQEEYOOAQQOOEYQAQOEEOOOAAQOQEYYOEOOQOOAEYEOOAEQYQOAEYYYAQAYOEYOEYYEEOEEOAYAEEQEQOAAAYAEYQQAYOYQQOAEAOQOOYAEEOAEQAQEEQYOOEEAEEAAOYQYQAOEQYOYEQEAAOYAQAQYEAQEQEEOQQQYEYOQ"
input_word = "BAANANAS"
counted = set()
length = len(input_word)
result = {PLAYER1: 0, PLAYER2: 0}


for i, letter in enumerate(input_word):
    if letter in VOWELS:
        player = PLAYER1
    else:
        player = PLAYER2
    prefix_table = get_prefix_table(input_word)
    for j in range(length-i):
        score = 0
        subst = input_word[i:j+i+1]
        prefixes = prefix_table[i:j + i + 1]
        if subst in counted:
            continue
        # score_gen = count_substrings(subst)
        if j == 0:
            score = input_word.count(subst)
        else:
            for s in substring_index(subst, input_word, prefixes):
                score += 1
        print(subst, score)
        counted.add(subst)
        result[player] += score
    counted.add(letter)

if result[PLAYER1] > result[PLAYER2]:
    print(PLAYER1, result[PLAYER1])
elif result[PLAYER1] < result[PLAYER2]:
    print(PLAYER2, result[PLAYER2])
else:
    print('Draw')
