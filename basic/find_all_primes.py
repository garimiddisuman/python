start = 0
end = 100

for i in range(start, end+1):
  factors = 0

  for j in range(1, i):
    if(i % j == 0):
      factors += 1

  if(factors == 1) :
    print(i)
