
word_list = {}
word_string = input("Enter string: ")

words = word_string.split()
for word in words:
    amount = word_list.get(word, 0)
    if amount is None:
        word_list[word] = 1
    else:
        word_list[word] = amount + 1

words = list(word_list.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_list[word]))

