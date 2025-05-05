string = "suman garimiddi"

vowels_set = "AEIOUaeiou"
vowels_count = 0

for string_index in range(len(string)):
  for vowels_set_index in range(len(vowels_set)):
    if(vowels_set[vowels_set_index] == string[string_index]):
      vowels_count += 1

print(vowels_count)
