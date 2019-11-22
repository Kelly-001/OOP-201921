# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: Kelly Luu
# date: 20-11-2019
# purpose: Lab 7

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3
        # new_word = self.user_input[0]+self.user_input[2]+self.user_input[1]+self.user_input[3:]
        # print(new_word)


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation
        sentence = self.user_input.split()
        print(sentence)

        for index, word in enumerate(sentence):
            temp_word=sentence[index]
            temp_word=temp_word[0]+temp_word[2]+temp_word[1]+temp_word[3:]
            sentence[index]=temp_word
        fixedsentence=" ".join(sentence)
        print(fixedsentence)

word_scrambler = WordScramble()
word_scrambler.scramble()

