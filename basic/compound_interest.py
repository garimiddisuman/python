principle = 1000
time = 2
rate = 5

compound_interest = 0
new_principle = principle

for i in range(time):
  compound_interest += (new_principle * rate) / 100
  new_principle = compound_interest + principle

print(compound_interest)
