# Q50 急がば回れ
# 長方形があり、一辺の長さが 1cm の正方形のマス目で区切られています。左上から右下まで移動する際、
# 同一直線上は２回しか移動できないものとします。また、必ずマス目の上を移動するものとし、同じ点をクロスして
# 進んでも構いません。このとき、左上から右下までの最長の経路を求めることを考えます。
# 縦が 5cm、横が 6cm の長方形の場合、最長の移動距離を求めてください。

from copy import deepcopy

def init_status(rows, cols):
  row_status = [[10] + [0] * cols + [10] for _ in range(rows + 1)]
  col_status = [[10] + [0] * rows + [10] for _ in range(cols + 1)]
  return {"hrz": row_status, "vrt": col_status}

# coord: (int, int), dx, dy: -1, 0, 1
# status["hrz"]: 横線の使用状況, status["vrt"]: 縦線の使用状況
# coord から (dx, dy) だけ移動してもよいか判定する
def cantgo(coord, dx, dy, status):
  x, y = coord
  if dx == 0:
    edges = status["vrt"]
    if sum(edges[x][1:-1]) > 1:
      return True
    if dy == 1:
      return edges[x][y+1] > 1
    elif dy == -1:
      return edges[x][y] > 1
  else:
    edges = status["hrz"]
    if sum(edges[y][1:-1]) > 1:
      return True
    if dx == 1:
      return edges[y][x+1] > 1
    elif dx == -1:
      return edges[y][x] > 1
  return True

# track: [coord], rows: 縦線の長さ, cols: 横線の長さ
# track から (dx, dy) へ移動して右下までたどり着く経路の総数を返す
def search(track, dx, dy, status, rows, cols):
  if cantgo(track[-1], dx, dy, status):
    return []
  x, y = track[-1]
  next_track = track + [(x+dx, y+dy)]
  if x+dx == cols and y+dy == rows:
    return [next_track]
  next_status = deepcopy(status)
  if dx != 0:
    next_status["hrz"][y][x + max(dx, 0)] += 1
  else:
    next_status["vrt"][x][y + max(dy, 0)] += 1
  tracks = search(next_track, 1, 0, next_status, rows, cols) + search(next_track, -1, 0, next_status, rows, cols)
  tracks += search(next_track, 0, 1, next_status, rows, cols) + search(next_track, 0, -1, next_status, rows, cols)
  return tracks

def main():
  rows, cols = 5, 6
  status = init_status(rows, cols)
  track = [(0, 0)]
  tracks = search(track, 1, 0, status, rows, cols)
  print("Search", len(tracks), "patterns")
  longest, length = track, 0
  for trk in tracks:
    if len(trk) - 1 > length:
      longest, length = trk, len(trk) - 1
  print("Longest:", longest)
  print("Length:", length)

if __name__ == '__main__':
  main()
