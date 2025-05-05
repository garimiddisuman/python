def factorial(num):
  if(num < 2):
    return 1
  
  fact = 1

  for i in range(2, num + 1):
    fact *= i
  
  return fact

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))