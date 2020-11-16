# Q69 男女平等な席替え
# ここでは「前後左右のいずれかに必ず異性が座る」ような席替えを考えます。男女それぞれ１５人の学級で 5 行 6 列の
# 座席で席替えを行います。上の条件を満たすような男女の配置が何通りあるかを求めてください。（左右、前後などの反転は
# 別々にカウントすることにします。また、個々の生徒がどこに座るかは無関係で、男女の配置のみを考えるものとします。）

from copy import deepcopy

# rows: int, cols: int
# (rows+2) * (cols+2) のサイズのリストを返す、初期値は -1 外枠（番兵）は -10 とする
def init_seat(rows, cols):
  seat = [[-10] * (cols + 2)]
  seat += [[-10] + [-1] * cols + [-10] for _ in range(rows)]
  seat.append([-10] * (cols + 2))
  return seat

# seat: [[int]], i: int, j: int
# seat の配置において、(i, j) 成分の前後左右に異性がいるかを判定する
def wrong_seat(seat, i, j):
  neighbors = [ seat[i-1][j], seat[i+1][j], seat[i][j-1], seat[i][j+1] ]
  if -1 in neighbors:
    return False
  else:
    opposite = 1 - seat[i][j]
    return not opposite in neighbors

# sex: 0 or 1 -> seat の (i, j) 成分の値を sex とした新しい seat を返す
def sit(seat, i, j, sex):
  result = deepcopy(seat)
  result[i][j] = sex
  return result

# seat をもとに、再帰的に配置の総数を探索する
def search(seat, rows, cols):
  seq = [s for s in sum(seat, []) if s > -10]
  m, f = seq.count(0), seq.count(1)
  if m + f == rows * cols:
    return 1
  idx = seq.index(-1)
  cnt, i, j = 0, idx // cols, idx % cols
  new_seat = sit(seat, i+1, j+1, 0)
  if not (m >= 15 or wrong_seat(new_seat, i+1, j+1)):
    cnt += search(new_seat, rows, cols)
  new_seat = sit(seat, i+1, j+1, 1)
  if not (f >= 15 or wrong_seat(new_seat, i+1, j+1)):
    cnt += search(new_seat, rows, cols)
  return cnt

def main():
  rows, cols = 3, 4
  seat = init_seat(rows, cols)
  print("Size: {:d} * {:d}".format(rows, cols))
  print("Total:", search(seat, rows, cols), "cases")

if __name__ == '__main__':
  main()
