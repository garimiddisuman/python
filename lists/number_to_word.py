SPACE = " "
EMPTY = ""

def get_word_less_than_twenty(number):
  words = ['', 'one', 'two', 'three', 'four', 'five', 'six','seven', 'eight','nine', 'ten', 'eleven', 'twelve', 'thirteen','fourteen', 'fifteen','sixteen', 'seventeen', 'eighteen','nineteen']
    
  return words[number]

def get_tens_word(number):
  tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty','sixty', 'seventy','eighty', 'ninety']

  if number < 20:
    return get_word_less_than_twenty(number)

  tens_part = number // 10
  ones_part = number % 10
  return (f"{tens[tens_part]} {get_word_less_than_twenty(ones_part)}").strip()

def get_words_less_than_thousand(number):
  if number < 100:
    return get_tens_word(number)

  hundreds_part = f"{get_word_less_than_twenty(number // 100)} hundred"
  remainder = number % 100

  if remainder == 0:
    return hundreds_part

  return f"{hundreds_part} and {get_tens_word(remainder)}"

def split_into_thousands(number):
  remaining = number
  parts = []

  while remaining > 0:
    parts.append(remaining % 1000)
    remaining = remaining // 1000

  return parts

def number_to_words(number):
  place_values = ["", "thousand", "million", "billion"]

  if number == 0:
    return "zero"

  parts = split_into_thousands(number)
  words_parts = []

  for index in range(len(parts)):
    part_words = get_words_less_than_thousand(parts[index])
    place = EMPTY if part_words == EMPTY else place_values[index]
    words_parts.insert(0, f"{part_words} {place}".strip())

  return SPACE.join(words_parts).strip()

def test_number_to_words(number, expected):
  actual = number_to_words(number)
  status = "✅" if actual == expected else "❌"
  print(f"{status} | {number} | {actual}")

def test_all():
  test_number_to_words(0, "zero")
  test_number_to_words(1, "one")
  test_number_to_words(10, "ten")
  test_number_to_words(15, "fifteen")
  test_number_to_words(16, "sixteen")
  test_number_to_words(21, "twenty one")
  test_number_to_words(91, "ninety one")
  test_number_to_words(100, "one hundred")
  test_number_to_words(101, "one hundred and one")
  test_number_to_words(900, "nine hundred")
  test_number_to_words(999, "nine hundred and ninety nine")
  test_number_to_words(1000, "one thousand")
  test_number_to_words(1001, "one thousand one")
  test_number_to_words(1010, "one thousand ten")
  test_number_to_words(1100, "one thousand one hundred")
  test_number_to_words(1011, "one thousand eleven")
  test_number_to_words(1101, "one thousand one hundred and one")
  test_number_to_words(10000, "ten thousand")
  test_number_to_words(10001, "ten thousand one")
  test_number_to_words(10010, "ten thousand ten")
  test_number_to_words(10011, "ten thousand eleven")
  test_number_to_words(10100, "ten thousand one hundred")
  test_number_to_words(10101, "ten thousand one hundred and one")
  test_number_to_words(22222, "twenty two thousand two hundred and twenty two")
  test_number_to_words(1000000, "one million")
  test_number_to_words(222222, "two hundred and twenty two thousand two hundred and twenty two")

test_all()
