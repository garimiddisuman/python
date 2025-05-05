string = "malayalam"

is_palindrome = True

for index in range(len(string) // 2):
  if(string[index] != string[-(index + 1)]):
    is_palindrome = False
    break

print(is_palindrome)