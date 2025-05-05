add = lambda a, b : a + b

print(add(2, 2))

def addition (a):
  return lambda b : a + b

add_one = addition(1)
add_two = addition(2)
print(add_one(1))
print(add_two(2))