string = "suman"

reversed_string = ""

for index in range(len(string) - 1, -1, -1):
  reversed_string += string[index]

print(reversed_string)