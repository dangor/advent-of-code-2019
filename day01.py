from functools import reduce

def p1(input):
  file = open(input)
  masses = list(int(x.strip('\n')) for x in file.readlines())
  file.close()

  sum = reduce(lambda x, y: x + int(y // 3 - 2), masses, 0)

  print(sum)