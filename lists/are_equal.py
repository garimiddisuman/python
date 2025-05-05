def are_equal(list1, list2):
  for index in range(len(list1)):
    if list1[index] != list2[index]:
      return False
  
  return True

def test_are_equal(list1, list2, expected):
  actual = are_equal(list1, list2)
  status = "✅" if actual == expected else "❌"
  print(f"{status} | {list1} & {list1} | {actual}")

def test_all():
  test_are_equal([1,2,3], [1,2,3], True)
  test_are_equal([1,2,3], [1,3, 2], False)

test_all()