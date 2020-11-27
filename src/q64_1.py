# Q64 迷路で待ち合わせ

move = [(-1,0), (0,1), (1,0), (0,-1)]

def init(size):
  maze = [[-1] * (size+2)]
  maze += [[-1] + [0]*size + [-1] for _ in range(size)]
  maze.append([-1] * (size+2))
  return maze

def create(num, size):
  walls = [idx for idx, ch in enumerate(bin(num)[::-1]) if ch == '1']
  maze = init(size)
  for n in walls:
    if 0 <= n < size ** 2:
      i, j = n // size, n % size
      maze[i+1][j+1] = 1
  return maze

def step(maze, plc, dir):
  for i in range(4):
    mv = (dir - 1 + i) % 4
    x, y = plc[0] + move[mv][0], plc[1] + move[mv][1]
    if maze[y+1][x+1] == 0:
      return (x, y), mv
  return plc, dir

def funcs(size):
  mask = (1 << (size * size)) - 1
  fs = [
    lambda m: (m >> 1) & int('0b' + ('0' + '1' * (size - 1)) * size, 2), # 右へ広げる
    lambda m: m << size & mask, # 上へ広げる
    lambda m: (m << 1) & int('0b' + ('1' * (size - 1) + '0') * size, 2), # 左へ広げる
    lambda m: m >> size # 下へ広げる
  ]
  return fs

# num: int, size: int -> bin(num) に対応する迷路が右下から左上までたどれるかを判定する
def enable(num, size):
  fs, mask = funcs(size), (1 << (size * size)) - 1
  man = (1 << (size * size - 1)) & (mask - num) # 右下からスタート
  while True:
    newm = man
    for f in fs:
      newm |= f(man) # 上下左右へ範囲を広げる
    newm &= (mask - num) # 壁以外のところを新しい範囲とする
    if newm & 1 == 1: # 左上へ到達
      return True
    if newm == man: # これ以上範囲が広がらない
      return False
    man = newm

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
  size = 5
  print("Size: {:d} * {:d}".format(size, size))
  candidates = [n for n in range(2, 2**(size*size), 2) if enable(n, size)]
  print("Maze:", len(candidates))
  cnt = 0
  for n in candidates:
    maze = create(n, size)
    if check(maze):
      cnt += 1
  print("Total:", cnt)

if __name__ == '__main__':
  main()
