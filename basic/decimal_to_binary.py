# decimal = 10
# binary = "" # 0101

# decimal = 1
# binary = 1

# decimal = 2
# binary = "";

while (decimal != 0):
  binary += str(decimal % 2)
  decimal = decimal // 2

print(binary)