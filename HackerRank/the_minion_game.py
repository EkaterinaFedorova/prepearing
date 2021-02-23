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

input_word = "BAANANAS"
length = len(input_word)
result = {PLAYER1: 0, PLAYER2: 0}


for i, letter in enumerate(input_word):
    if letter in VOWELS:
        player = PLAYER1
    else:
        player = PLAYER2
    score = length - i
    result[player] += score

if result[PLAYER1] > result[PLAYER2]:
    print(PLAYER1, result[PLAYER1])
elif result[PLAYER1] < result[PLAYER2]:
    print(PLAYER2, result[PLAYER2])
else:
    print('Draw')
