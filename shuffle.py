import random

def shuffle(arr1, arr2):
  deck = arr1 + arr2
  scram = random.sample(deck, k=len(deck))
  return scram

def multishuffle(deck, k):
  if k < 1:
    return deck
  else:
    mid = len(deck) // 2
    left = deck[:mid]
    right = deck[mid:]
    scram = shuffle(left, right)
    k += -1
    return multishuffle(scram, k)

if __name__ == '__main__':
  from collections import Counter
  left = ['delver of secrets', 'island', 'steam vents', 'brainstorm']
  right = ['mountain', 'lightning bolt', 'young pyromancer', 'force of will']
  deck = shuffle(left, right)
  first = []
  trials = 100
  for i in range(trials):
    temp = multishuffle(deck, 2)
    first.append(temp[0])
    deck = temp
  c = Counter(first)
  print(f'FIRST DRAW IN {trials} TRIALS:\n', c)

