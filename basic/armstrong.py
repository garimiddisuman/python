number = 153

sum = 0
candidate = number

while candidate > 0:
  remainder = candidate % 10
  sum += (remainder * remainder * remainder)
  candidate = candidate // 10

print(sum == number)