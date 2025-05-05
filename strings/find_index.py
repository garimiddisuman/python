string = "suman"
target = "a"

index = 0

while index < len(string):
  if(string[index] == target):
    break
  index += 1

if(index == len(string)):
  print(-1)
else :
 print(index)