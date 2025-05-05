nth = 8

current_term = 0
next_term = 1

for i in range(nth):
  print(current_term)
  sum = current_term + next_term
  current_term = next_term
  next_term = sum