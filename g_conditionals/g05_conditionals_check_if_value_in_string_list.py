sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

if word.lower() in sentence.lower():
  print('The word is in the sentence')
else:
  print('The word is not in the sentence')


nums = [1, 2, 3, 4]

if 3 in nums:
  print('The number was found')
else:
  print('The number was not found')


#exercise solved
def value_in_string():
    sentence = 'Python is the best!'

    if 'best' in sentence:
        print('The word is in the sentence')
    else:
        print('The word is not in the sentence')

value_in_string()
