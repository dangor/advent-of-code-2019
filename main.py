import time
import day01, day02

p1, p2 = 'p1', 'p2'
def run(module, p, input):
  start = time.time()

  print(f"\n{module.__name__} {p}:")
  getattr(module, p)(input)

  end = time.time()
  print(f"(t={end - start})")

run(day01, p1, "inputs/day01.txt")
run(day01, p2, "inputs/day01.txt")
day02.test()
run(day02, p1, "inputs/day02.txt")
