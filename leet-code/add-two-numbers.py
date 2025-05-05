# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

def compute_digit_and_carry(carry_in, digit_sum):
  digit = (digit_sum + carry_in) % 10
  carry = (digit_sum + carry_in) // 10
  return digit, carry

def add_digits_at_index(index, l1, l2, result, carry):
  digit1 = l1[index] if index < len(l1) else 0
  digit2 = l2[index] if index < len(l2) else 0
  digit, carry = compute_digit_and_carry(carry, digit1 + digit2)
  result.append(digit)
  return carry

def add_two_numbers(l1, l2):
  carry = 0
  result = []
  max_length = max(len(l1), len(l2))

  for index in range(max_length):
    carry = add_digits_at_index(index, l1, l2, result, carry)

  if carry != 0:
    result.append(carry)

  return result

print(add_two_numbers([2,4,3], [5,6,4]))
print(add_two_numbers([0], [0]))
print(add_two_numbers([9,9,9,9,9,9,9], [9,9,9,9]))

## Another approach
