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
# VOWELS = "AEIOU"
# PLAYER1 = 'Kevin'
# PLAYER2 = 'Stuart'
#
# input_word = input()
# counted = set()
# length = len(input_word)
# result = {PLAYER1: 0, PLAYER2: 0}

"BANANABANAN"
# B
# BA
# BAN
# BANA



def get_prefix_table(pattern):
    table = [0]
    pattern_length = len(pattern)
    for i in range(1, pattern_length):
        j = 0
        while pattern[i] == pattern[j] and j < pattern_length:
            j += 1
        table.append(j)

    return table

def substring_index(needle, haystack):
    prefix_table = get_prefix_table(needle)
    haystack_length = len(haystack)
    i = 0
    while i < haystack_length:
        j = 0
        while haystack[i+j] == needle[j]:
            j += 1
            if len(needle) == j:
                print("FIND {0}".format(i))
                # return i
                break
                yield i

        prefix_length = prefix_table[j-1]
        if prefix_length > 0:
            i += prefix_length
            j += prefix_length
        else:
            i += 1
        if i + j > haystack_length:
            break
    return -1

for i in substring_index("ANAN", "BANANAN"):
# for i in substring_index("YBYBO", "YBOYYBYBOXYBYBO"):
    print(i)

#
# def count_substrings(substring, main_str=input_word):
#     # substring_re = '(?=({0}))'.format(re.escape(substring))
#     # return len(re.findall(substring_re, main_str))
#     start = 0
#     while True:
#         start = main_str.find(substring, start)
#         if start == -1:
#             return
#         yield start
#         start += 1
#
# for i, letter in enumerate(input_word):
#     if letter in VOWELS:
#         player = PLAYER1
#     else:
#         player = PLAYER2
#
#     for j in range(length-i):
#         score = 0
#         subst = input_word[i:j+i+1]
#         if subst in counted:
#             continue
#         # score_gen = count_substrings(subst)
#         for s in count_substrings(subst):
#             score += 1
#
#         counted.add(subst)
#         result[player] += score
#     counted.add(letter)
#
# if result[PLAYER1] > result[PLAYER2]:
#     print(PLAYER1, result[PLAYER1])
# elif result[PLAYER1] < result[PLAYER2]:
#     print(PLAYER2, result[PLAYER2])
# else:
#     print('Draw')


