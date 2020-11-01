# Q50 急がば回れ

from copy import deepcopy

def init_status(rows, cols):
  row_status = [0] * (rows + 1)
  col_status = [0] * (cols + 1)
  return {"hrz": row_status, "vrt": col_status}

# coord: (int, int), dx, dy: -1, 0, 1
# status["hrz"]: 横線の使用状況, status["vrt"]: 縦線の使用状況
# coord から (dx, dy) だけ移動してもよいか判定する
def cantgo(coord, dx, dy, status, rows, cols):
  x, y = coord
  if dx == 0:
    if status["vrt"][x] > 1:
      return True
    if y + dy < 0 or y + dy > rows:
      return True
  else:
    if status["hrz"][y] > 1:
      return True
    if x + dx < 0 or x + dx > cols:
      return True
  return False

# track: [coord], rows: 縦線の長さ, cols: 横線の長さ
# track から (dx, dy) へ移動して右下までたどり着く経路の総数を返す
def search(track, dx, dy, status, rows, cols):
  if cantgo(track[-1], dx, dy, status, rows, cols):
    return []
  x, y = track[-1]
  next_track = track + [(x+dx, y+dy)]
  if x + dx == cols and y + dy == rows:
    return [next_track]
  next_status = deepcopy(status)
  if dx == 0:
    next_status["vrt"][x] += 1
  else:
    next_status["hrz"][y] += 1
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
