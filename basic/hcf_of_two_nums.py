num1 = 24
num2 = 16

hcf = num2

while True :
  remainder = num1 % hcf
  
  if(remainder == 0):
    break

  num1 = hcf
  hcf = remainder

print(hcf)