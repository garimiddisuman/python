sentence = "   This   is a   sentence  "

replaced_sentence = ""

for index in range(len(sentence)):
  if(sentence[index] == " "):
    replaced_sentence += "_"
    continue

  replaced_sentence += sentence[index]

print(replaced_sentence)