def square (n):
  return n * n

nums = [1,2,3,4,5]
print(list(map(square, nums)))

def is_even (n):
  return not n % 2

nums = [1,2,3,4,5,6,7,8]
print(list(filter(is_even, nums)))