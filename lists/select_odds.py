def select_odds(list):
  odds = []

  for index in range(len(list)):
    if list[index] % 2:
      odds.append(list[index])

  return odds

print(select_odds([1,2,3,4,5,6,7,8]))