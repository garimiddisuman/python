num = 90

factors = 0

while(factors != 1) :
  num += 1
  factors = 0

  for i in range(1, num):
    if(num % i == 0):
      factors += 1

print(num)