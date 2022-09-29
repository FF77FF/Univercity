words = input()
first_word = words[:words.find(' ')]
second_word = words[words.find(' ') + 1:]
print(second_word + ' ' + first_word)
