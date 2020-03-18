import random

def add_char(char, num):
     asc = ord(char)
     asc -= 97
     next = (asc + num) % 26
     return chr(next + 97)

def random_char():
     roll1 = random.randint(0, 25)
     roll2 = random.randint(0, 1009)
     letter = chr(roll1 + 97)
     return add_char(letter, roll2)

def random_word(wordLength):
     for x in range(wordLength):
          if (x == 0):
               newWord = ''
          newWord += random_char()
     return newWord

def random_sentence(num = 1):
     for i in range(num):
          if i == 0:
               text = ''
          s_len = random.randint(2, 10)
          for j in range(s_len):
               w_len = random.randint(1, 9)
               if j == 0:
                   text += random_word(w_len).capitalize()
               else:
                   text += random_word(w_len)
               if (j == (s_len-1)):
                    text += '. '
               else:
                    text += ' '
     return text    
