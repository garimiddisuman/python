number = 12

temp = number
potential_factor = 2

while temp >= potential_factor:
  if(temp % potential_factor == 0):
    print(potential_factor)
    temp = temp // potential_factor
    continue

  potential_factor += 1
