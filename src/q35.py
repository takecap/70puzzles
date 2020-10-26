# Q35 運命の出会いは何通り？
# 男性は左上から右下まで、女性は右下から左上までそれぞれ最短距離を同じスピードで移動します。このとき、
# 1. 同一直線内の頂点に同時に止まる（お互いが見える）ことが２度発生する
# 2. 同じ頂点で同時に重なる（お互いに接触した状態）
# のような場合に「運命の出会い」があったということにします。一辺の長さが 6cm の正方形の場合、
# 「運命の出会い」が起きるのは何通りあるかを求めてください。

# size: 正方形の一辺の長さ
# 左上 (0, 0) -> 右下 (size, size) まで移動するパターンのリストを返す
def init_patterns(size):
  def step(track):
    coord = track[-1]
    if coord == (size, size):
      return [track]
    results = []
    if coord[0] < size:
      results += step(track + [(coord[0]+1, coord[1])])
    if coord[1] < size:
      results += step(track + [(coord[0], coord[1]+1)])
    return results
  return step([(0,0)])

# mtrack: 男性の経路, ftrack: 女性の経路
# mtrack と ftrack が「運命の出会い」であるかどうかを判定する
def check(mtrack, ftrack):
  count = 0
  for m, f in zip(mtrack, ftrack):
    if m[0] == f[0]:
      count += 1
    if m[1] == f[1]:
      count += 1
    if count > 1:
      return True
  return False

def main():
  size = 6
  ftracks = init_patterns(size)
  mtracks = [track[::-1] for track in ftracks]
  count = 0
  for ftr in ftracks:
    for mtr in mtracks:
      if check(mtr, ftr):
        count += 1
  print("Size:", size, "Count:", count)

if __name__ == '__main__':
  main()
