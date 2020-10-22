# Q27 右折を禁止されても大丈夫？

# status["hrz"]: 横向きの edge の利用状況を１次元のリストで表現する
# status["vrt"]: 縦向きの edge の利用状況を１次元のリストで表現する
def init_status(rows, cols):
  row_status = [0] * (rows + 1) * cols
  col_status = [0] * rows * (cols + 1)
  return {"hrz": row_status, "vrt": col_status}

# tgt: "hrz" or "vrt", idx: int
# status[tgt] を利用済（0 -> 1）にした新しい status を返す
def use_edge(status, tgt, idx):
  results = {"hrz": status["hrz"], "vrt": status["vrt"]}
  if idx == 0:
    results[tgt] = [1] + status[tgt][1:]
  elif idx == len(status[tgt]) - 1:
    results[tgt] = status[tgt][:-1] + [1]
  else:
    results[tgt] = status[tgt][:idx] + [1] + status[tgt][idx+1:]
  return results

# 格子点 (x, y) から dir 方向へ移動可能かを調べる
# 移動可能なら (dx, dy) 及び移動する edge の情報 tgt と idx を返す
# 移動不可なら idx = -1 を返す
def calc(x, y, dir, rows, cols):
  dx, dy, tgt, idx = 0, 0, '', -1
  if dir == 0 and y < rows: # 上
    tgt, dy, idx = "vrt", 1, y * (cols + 1) + x
  elif dir == 2 and y > 0: # 下
    tgt, dy, idx = "vrt", -1, (y - 1) * (cols + 1) + x
  elif dir == 1 and x > 0: # 左
    tgt, dx, idx = "hrz", -1, (x - 1) * (rows + 1) + y
  elif dir == 3 and x < cols: # 右
    tgt, dx, idx = "hrz", 1, x * (rows + 1) + y
  return dx, dy, tgt, idx

# (x, y) から dir 方向を向いている状態からスタートして goal に到達する道順の数 count を返す
# dir 方向及び dir + 1 方向（左折）それぞれについて、再帰的に探索を行う
def search(x, y, dir, status, rows, cols):
  if x == cols and y == rows: # goal に到達
    return 1
  count = 0
  dx, dy, tgt, idx = calc(x, y, dir, rows, cols) # dir 方向への移動を試す
  if 0 <= idx < len(status[tgt]) and status[tgt][idx] == 0:
    new_status = use_edge(status, tgt, idx)
    count += search(x+dx, y+dy, dir, new_status, rows, cols)
  dir = (dir + 1) % 4 # 左折
  dx, dy, tgt, idx = calc(x, y, dir, rows, cols)
  if 0 <= idx < len(status[tgt]) and status[tgt][idx] == 0:
    new_status = use_edge(status, tgt, idx)
    count += search(x+dx, y+dy, dir, new_status, rows, cols)
  return count

def main():
  x, y, dir, rows, cols = 0, 0, 3, 4, 6
  status = init_status(rows, cols)
  count = search(x, y, dir, status, rows, cols)
  print("{:d} * {:d}: {:d} count".format(rows, cols, count))

if __name__ == '__main__':
  main()
