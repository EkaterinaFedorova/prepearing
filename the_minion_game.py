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
import re

VOWELS = "AEIOU"
PLAYER1 = 'Kevin'
PLAYER2 = 'Stuart'

input_word = input()
counted = set()
length = len(input_word)
result = {PLAYER1: 0, PLAYER2: 0}


def count_substrings(substring, main_str=input_word):
    # substring_re = '(?=({0}))'.format(re.escape(substring))
    # return len(re.findall(substring_re, main_str))
    start = 0
    while True:
        start = main_str.find(substring, start)
        if start == -1:
            return
        yield start
        start += 1

for i, letter in enumerate(input_word):
    if letter in VOWELS:
        player = PLAYER1
    else:
        player = PLAYER2

    for j in range(length-i):
        score = 0
        subst = input_word[i:j+i+1]
        if subst in counted:
            continue
        # score_gen = count_substrings(subst)
        for s in count_substrings(subst):
            score += 1

        counted.add(subst)
        result[player] += score
    counted.add(letter)

if result[PLAYER1] > result[PLAYER2]:
    print(PLAYER1, result[PLAYER1])
elif result[PLAYER1] < result[PLAYER2]:
    print(PLAYER2, result[PLAYER2])
else:
    print('Draw')
