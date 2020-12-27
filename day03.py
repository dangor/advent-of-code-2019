from test import build_test

def p1(input):
  file = open(input)
  lines = list(x.strip('\n') for x in file.readlines())
  file.close()

  nearest = nearest_intersection(lines)
  print(nearest)

def nearest_intersection(lines):
  path1 = get_path(lines[0])
  path2 = get_path(lines[1])
  intersections = path1.intersection(path2)
  nearest = None
  for intersection in intersections:
    distance = abs(intersection[0]) + abs(intersection[1])
    if nearest == None or distance < nearest:
      nearest = distance
  return nearest

def get_path(line):
  path = set()
  cur = (0,0)
  offsets = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, -1),
    'U': (0, 1)
  }
  for instruction in line.split(','):
    direction = instruction[0]
    offset = offsets[direction]
    distance = int(instruction[1:])
    for i in range(distance):
      cur = (cur[0] + offset[0], cur[1] + offset[1])
      path.add(cur)
  return path

def test():
  test_case = build_test(nearest_intersection)
  test_case(["R8,U5,L5,D3","U7,R6,D4,L4"], 6)
  test_case(["R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83"], 159)
  test_case(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"], 135)
