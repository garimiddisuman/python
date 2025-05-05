def slice(string, start, end):
  start_index = max(0, start)
  end_index = min(end + 1, len(string))
  substring = ""

  for i in range(start_index, end_index):
    substring += string[i]
  
  return substring

print(slice('suman', 1, 4))