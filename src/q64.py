# Q64 迷路で待ち合わせ
# 縦と横に n 個並んでいるマスの幾つかを塗りつぶして、迷路を作ります。塗りつぶしたところが壁になり、
# 塗りつぶされていないところが通路になります。２人がそれぞれA地点とB地点を同時にスタートして、
# 一度に１マスずつ、「右手法」で進みます。このとき、２人が途中で出会うパターンが何通りあるかを考えます。
# n = 5 のとき、途中で出会うような迷路のパターンが何通りあるかを求めてください。

from copy import deepcopy
move = [(-1,0), (0,1), (1,0), (0,-1)]

# size: int -> (rows+2) * (cols+2) のサイズのリストで迷路を表す、外枠は -1
def init(size):
  maze = [[-1] * (size+2)]
  maze += [[-1] + [0]*size + [-1] for _ in range(size)]
  maze.append([-1] * (size+2))
  return maze

# num: int -> bin(num) の 1 に対応する壁のある迷路を返す
def create(num, size):
  walls = [idx for idx, ch in enumerate(bin(num)[::-1]) if ch == '1']
  maze = init(size)
  for n in walls:
    if 0 <= n < size ** 2:
      i, j = n // size, n % size
      maze[i+1][j+1] = 1
  return maze

# plc: (x, y), dir: 0,1,2,3 -> 右手法での次の位置・向きを返す
def step(maze, plc, dir):
  for i in range(4):
    mv = (dir - 1 + i) % 4
    x, y = plc[0] + move[mv][0], plc[1] + move[mv][1]
    if maze[y+1][x+1] == 0:
      return (x, y), mv
  return plc, dir

# 与えられた maze が有効（ゴールまでたどれる）かどうかを判定する
def connection(maze, size):
  results, diff = set(), {(1,1)}
  while diff != set():
    results |= diff
    temp = set()
    for x, y in diff:
      if maze[y][x-1] == 0:
        temp.add((x-1, y))
      if maze[y][x+1] == 0:
        temp.add((x+1, y))
      if maze[y-1][x] == 0:
        temp.add((x, y-1))
      if maze[y+1][x] == 0:
        temp.add((x, y+1))
    if (size, size) in temp:
      return True
    diff = temp - results
  return False

# 与えられた maze で、ABが途中で出会うかどうかを判定する
def check(maze):
  size = len(maze) - 2
  plcA, dirA = (0,0), 1
  plcB, dirB = (size-1, size-1), 3
  while plcA != (size-1, size-1) and plcB != (0,0):
    plcA, dirA = step(maze, plcA, dirA)
    plcB, dirB = step(maze, plcB, dirB)
    if plcA == plcB:
      return True
  return False

def main():
  size = 4
  print("Size: {:d} * {:d}".format(size, size))
  candidates = [n for n in range(2, 2**(size*size), 2) if connection(create(n, size), size)]
  print("Maze:", len(candidates))
  cnt = 0
  for n in candidates:
    maze = create(n, size)
    if check(maze):
      cnt += 1
  print("Total:", cnt)

if __name__ == '__main__':
  main()
