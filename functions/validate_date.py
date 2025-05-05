YMD = "YYYY-MM-DD"
MDY = "MM-DD-YYYY"
DMY = "DD-MM-YYYY"
INVALID_FORMAT = "invalid format"
HYPHEN = "-"
DATE_NOT_ACCORDING_TO_FORMAT = "date not according to format"
INVALID_MONTH = "invalid month"
INVALID_YEAR = "invalid year"
INVALID_DAY = "invalid day"

def is_date_according_to_format(format, date):
  if len(date) != 10:
    return False
  
  for index in range(len(format)):
    if format[index] == HYPHEN and date[index] != HYPHEN:
      return False
    
    if format[index] != HYPHEN and not date[index].isdigit():
      return False

  return True

def get_default_format(format, date):
  if format == YMD:
    return date
  
  return f"{date[6:]}-{date[:5]}"

def is_valid_format (format) :
  return format == YMD or format == MDY or format == DMY

def parse_day(date):
  return date[-2:]

def parse_month(date):
  return date[5:7]

def parse_year(date):
  return date[:4]

def get_max_days(month):
  return 31 - ((month - 1) % 7) % 2

def is_valid_month(month):
  return month > 0 and month < 13

def is_valid_year(year):
  return year > 0 and year <= 9999

def is_leap_year(year):
  if year % 400 == 0:
    return True
  
  return year % 4 == 0 and year % 100 != 0

def validate_feb(year, day):
  if is_leap_year(year):
    return day > 0 and day < 30
  
  return day > 0 and day < 29

def is_valid_day(year, month, day):
  if month == 2:
    return True if validate_feb(year, day) else INVALID_DAY
  
  max_days = get_max_days(month)
  is_valid = day > 0 and day <= max_days

  if not is_valid:
    return INVALID_DAY
  
  return True

def validate_YMD(day, month, year):
  if not is_valid_year(year):
    return INVALID_YEAR
  
  if not is_valid_month(month):
    return INVALID_MONTH
  
  return is_valid_day(year, month, day)

def is_valid_date(format, date):
  day = int(parse_day(date))
  month = int(parse_month(date))
  year = int(parse_year(date))

  if format == DMY:
    day,month = month,day
  
  return validate_YMD(day, month, year)

def validate(format, date):
  if not is_valid_format(format):
    return INVALID_FORMAT
  
  if not is_date_according_to_format(format, date):
    return DATE_NOT_ACCORDING_TO_FORMAT
  
  default_format = get_default_format(format, date)
  return is_valid_date(format, default_format)

def test_validate(format, date, expected):
  actual = validate(format, date)
  status = "✅" if actual == expected else "❌"
  print(f"{status} | {date} | {actual}")

def test_all():
  test_validate("ABC-CDF-asd", "12-34-2004", "invalid format")
  test_validate("YYYY-MM-DD", "20-2024-41", "date not according to format")
  test_validate("MM-DD-YYYY", "20-2024-41", "date not according to format")
  test_validate("DD-MM-YYYY", "20-2024-41", "date not according to format")
  test_validate("YYYY-MM-DD", "2024-4a-41", "date not according to format")
  test_validate("MM-DD-YYYY", "2q-42-100", "date not according to format")
  test_validate("DD-MM-YYYY", "20-2024-4k", "date not according to format")
  test_validate("DD-MM-YYYY", "20-02-2024", True)
  test_validate("DD-MM-YYYY", "20-13-2000", "invalid month")
  test_validate("MM-DD-YYYY", "12-12-1000", True)
  test_validate("MM-DD-YYYY", "44-42-1000", "invalid month")
  test_validate("YYYY-MM-DD", "2024-40-41", "invalid month")
  test_validate("YYYY-MM-DD", "2024-12-31", True)
  test_validate("YYYY-MM-DD", "2024-02-31", "invalid day")

test_all()