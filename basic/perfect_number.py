number = 28
factors_sum = 1

for potential_factor in range(2, number) :
  if(number % potential_factor == 0):
    factors_sum += potential_factor

print(factors_sum == number)
