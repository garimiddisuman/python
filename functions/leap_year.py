def is_leap_year(year):
  if(year % 400 == 0) :
    return True
  
  return year % 4 == 0 and year % 100 != 0

print(is_leap_year(2024))