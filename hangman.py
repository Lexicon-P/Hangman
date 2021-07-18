import random
from words import words

HANGMAN_PICS = ['''
  +----+
       |
       |
       |
    =======''', '''
  +----+
  O    |
       |
       |
   =======''', '''
 +----+
 O    |
 |    |
      |
   =======''', '''
 +----+
 O    |
/|    |
      |
  =======''', '''
 +----+
 O    |
/|\   |
      |
 =======''', '''
 +----+
 O    |
/|\   |
/     |
=======''', '''
 +----+
 O    |
/|\   |
/ \   |
=======''']

def get_secret_word(words):
    word = random.choice(words)         #selects a random word from the words list
    while ' ' in word or '-' in word:   #ensures that the word does not contain a space or -
        word = random.choice(words)
    return word.upper()                 #returns the secret word in upper case
