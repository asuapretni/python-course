sentence = 'The quick brown fox jumps over the lazy dog.'

query = sentence.find('quick')  # 4
query_two = sentence.index('quick')  # 4

query = sentence.find('oops')  # -1
query_two = sentence.index('oops')  # ERROR


# More used
query_three = 'quick' in sentence # True
query_three = 'oops' in sentence # False