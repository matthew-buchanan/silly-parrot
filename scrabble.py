import random
import ascii_math as am

scrabble = {
     'e': 12, 'a': 9, 'i': 9, 'o': 8, 'n': 6, 'r': 6,
     't': 6, 'l': 4, 's': 4, 'u': 4, 'd': 4, 'g': 3,
     'b': 2, 'c': 2, 'm': 2, 'p': 2, 'f': 2, 'h': 2,
     'v': 2, 'w': 2, 'y': 2, 'k': 1, 'j': 1, 'x':1,
     'q': 1, 'z': 1, 'blank': 2 
     }
scrabbleRanges = {}
for item in scrabble:
     if (item == 'e'):
          count = 0
     scrabbleRanges[item] = range(count, count + scrabble[item])
     count += scrabble[item]
totalLetters = sum(scrabble.values())


def scrabble_char():
     roll = random.randint(0, totalLetters-1)
     for x in scrabbleRanges:
          if roll in scrabbleRanges[x]:
               if x == 'blank':
                    return am.random_char()
               else:
                    return x


def scrabble_word(wordLength):
     for x in range(wordLength):
          if x == 0:
               newWord = ''
          newWord += scrabble_char()
     return newWord 

def scrabble_sentence(num = 1):
     for i in range(num):
          if i == 0:
               text = ''
          s_len = random.randint(2, 10)
          for j in range(s_len):
               w_len = random.randint(1, 9)
               if j == 0:
                   text += scrabble_word(w_len).capitalize()
               else:
                   text += scrabble_word(w_len)
               if (j == (s_len-1)):
                    text += '. '
               else:
                    text += ' '
     return text    
