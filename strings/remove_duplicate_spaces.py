sentence = "    This    is    a     sentence     "

start_index = 0
end_index = len(sentence) - 1
SPACE = " "

while start_index < len(sentence) and sentence[start_index] == SPACE:
  start_index += 1

while end_index >= 0 and sentence[end_index] == SPACE:
  end_index -= 1

single_space_sentence = ""

for index in range(start_index, end_index + 1):
  if(sentence[index] == SPACE and sentence[index + 1] == SPACE):
    continue

  single_space_sentence += sentence[index]

print(f"Input : >{sentence}<")
print(f"Output : >{single_space_sentence}<")