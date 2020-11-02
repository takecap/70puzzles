# Q52 同時に終わる砂時計
# Ｎ個の砂時計があり、それぞれ１分〰Ｎ分を計測できます。これらを円形に並べ、１分ごとに逆さにしていきます。
# このとき、逆さにする砂時計の開始位置は、「時計回りに１つずつ移動」し、個数は開始位置の砂時計の計測分数によって
# 変わります（１分の砂時計の場合は１個、Ｎ分の砂時計の場合はＮ個を時計回りに連続して逆さにしていきます）。
# N = 8 のとき、全ての砂が同時に下に落ちるような８個の砂時計の配置を求め、その並べ方の総数を答えてください。
# 同じ並び順でも、逆さにする砂時計の開始位置が違う場合は別々に数えるものとします。

from itertools import permutations

# volumes: (int), clocks: (int), num: int
# volumes が各砂時計の現在の残り時間を表す int のタプル、clocks が各砂時計の容量を表す int のタプル
# num 番目の砂時計を基点に逆さにした結果を返す
def step(volumes, clocks, num):
  size = len(clocks)
  volumes = [max(vol-1, 0) for vol in volumes]
  for i in range(clocks[num]):
    idx = (num + i) % size
    volumes[idx] = clocks[idx] - volumes[idx]
  return tuple(volumes), (num + 1) % size

# clocks の並び順で逆さにする開始位置を idx 番目としたとき、全ての砂が同時に下に落ちるかどうかを判定する
def finish(clocks, idx):
  size = len(clocks)
  volumes, goal = tuple(vol for vol in clocks), (1, ) * size
  results = { (volumes, idx) }
  while True:
    volumes, idx = step(volumes, clocks, idx)
    if volumes == goal:
      return True
    if (volumes, idx) in results:
      return False
    else:
      results.add((volumes, idx))

def main():
  num = 8
  clocks_list = [ (1, ) + pm for pm in permutations(range(2, num+1), num-1)]
  flist = []
  flag = 2
  for clocks in clocks_list:
    for i in range(num):
      if finish(clocks, i):
        flist.append((clocks, i))
    if clocks[1] != flag:
      print("DONE", flag, len(flist))
      flag = clocks[1]
  print("TOTAL:", len(flist))

if __name__ == '__main__':
  main()
