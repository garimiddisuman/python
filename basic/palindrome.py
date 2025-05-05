number = 151

reversed_number = number
result = 0

while reversed_number > 0:
  remainder = reversed_number % 10
  result = (result * 10) + remainder
  reversed_number = reversed_number // 10

print(result == number)