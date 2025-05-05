def power_set(lst):
  sub_sets = [[]]

  for element in lst:
    sub_sets += [subset + [element] for subset in sub_sets]

  return sub_sets

print(power_set([]))
print(power_set([1]))
print(power_set([1,2]))
print(power_set([1,2,3]))