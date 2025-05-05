sentence = "    This    is    a     sentence     "

words_count = 0
SPACE = " "
copy_sentence = SPACE + sentence

for index in range(len(copy_sentence) - 1):
  if(copy_sentence[index] == SPACE and copy_sentence[index + 1] != SPACE):
    words_count += 1

print(words_count)