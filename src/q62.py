# Q62 交差せずに一筆書き
# 横に m 個、縦に n 個の格子点が並んでいます。このすべての点を一筆書きで結ぶことを考えます。
# ただし、縦と横の隣り合う点を直線で結ぶのみとし、交差してはいけないものとします。
# m = 5, n = 4 のとき、全部で何通りの方法があるかを求めてください。
# （始点と終点が逆なだけで、同じ位置・同じ形である場合は１つと数えますが、
# 左右などの反転で形だけ同じ（位置が違う）場合は別々のものとカウントします。

# seq: (int), dir: 0,1,2,3, rows: int, cols: int
# seq に続けて、dir 方向へ進んだ時の次の格子点の idx を返す
# 進行不能のときは -1 を返す
def step(seq, dir, rows, cols):
  now, nxt = seq[-1], -1
  x, y = now % cols, now // cols
  if dir == 0 and y > 0: # 上
    nxt = now - cols
  elif dir == 1 and x > 0: # 左
    nxt = now -1
  elif dir == 2 and y < rows - 1: # 下
    nxt = now + cols
  elif dir == 3 and x < cols - 1: # 右
    nxt = now + 1
  if nxt in seq:
    return -1
  else:
    return nxt

# seq から始めて、一筆書きで得られる seq の集合を返す
def search(seq, rows, cols):
  if len(seq) == rows * cols:
    return {seq, seq[::-1]}
  results = set()
  for i in range(4):
    nxt = step(seq, i, rows, cols)
    if nxt > -1:
      results |= search(seq + (nxt, ), rows, cols)
  return results

def main():
  m, n = 4, 5
  results = set()
  for i in range(m * n):
    results |= search((i, ), m, n)
  print("Total:", len(results) // 2, 'cases')

if __name__ == '__main__':
  main()
