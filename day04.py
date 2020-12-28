from test import build_test

def p1(input):
  output = num_valid(input)
  print(output)

def num_valid(input):
  lower, upper = input[0], input[1]
  count = 0
  for i in range(lower, upper + 1):
    if is_valid(i):
      count += 1
  return count

def is_valid(num):
  has_double = False
  previous_digit = None
  digit_mask = 100000
  remaining = num
  while digit_mask > 0:
    digit = remaining // digit_mask

    if previous_digit != None and previous_digit == digit:
      has_double = True

    if previous_digit != None and previous_digit > digit:
      return False # decreasing
    
    previous_digit = digit

    remaining %= digit_mask
    digit_mask //= 10
  return has_double

def test():
  test_case = build_test(is_valid)
  test_case(122345, True)
  test_case(111111, True)
  test_case(223450, False)
  test_case(123789, False)
