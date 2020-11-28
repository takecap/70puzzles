# 男女平等な席替え

# cols: int,  r1, r2, r3: 0..2**cols-1
# (r1, r2) の後に r3 を配置できるかを判定する
def check(r1, r2, r3, cols):
  all, mask1, mask2 = 2**cols-1, 7 << (cols-2), 1 << (cols-1)
  for i in range(cols):
    # m1: 左から i 番目の左右に男子が並んでいるかを判定するためのマスク
    # m2: 左から i 番目の上下に男子が並んでいるかを判定するためのマスク
    m1, m2 = (mask1 >> i) & all, (mask2 >> i) & all
    if r1 & m2 == m2 and r2 & m1 == m1 and r3 & m2 == m2:
      return False
    if (r1 ^ all) & m2 == m2 and (r2 ^ all) & m1 == m1 and (r3 ^ all) & m2 == m2: # r ^ all -> r を反転することで、女子の並びを探索する
      return False
  return True

# (r1, r2) の跡に配置できる r3 のリストを返すような辞書を作成する
def next_rows(cols):
  oks = {}
  for r1 in range(2**cols):
    for r2 in range(2**cols):
      oks[r1, r2] = [r3 for r3 in range(2**cols) if check(r1, r2, r3, cols)]
  return oks

# row_num: 現在の行数, used: 現在の男子の人数 -> ここから rows 行までの配置の総数を探索する
def search(r1, r2, row_num, used, cols, rows, nexts, memo):
  if (r1, r2, row_num, used) in memo:
    return memo[r1, r2, row_num, used]
  if row_num == rows:
    memo[r1, r2, row_num, used] = 1
    return memo[r1, r2, row_num, used]
  size, cnt = rows*cols, 0
  if row_num == rows - 1:
    for r in nexts[r1, r2]:
      m = bin(r).count('1')
      if r2 in nexts[r, r] and used + m == size // 2:
        cnt += search(r2, r, row_num+1, used+m, cols, rows, nexts, memo)
  else:
    for r in nexts[r1, r2]:
      m = bin(r).count('1')
      if used + m <= size // 2:
        cnt += search(r2, r, row_num+1, used+m, cols, rows, nexts, memo)
  memo[r1, r2, row_num, used] = cnt
  return cnt

def main():
  nexts, memo, count = next_rows(6), {}, 0
  for r in range(2**6):
    mens = bin(r).count('1')
    count += search(r, r, 1, mens, 6, 5, nexts, memo)
  print("Total:", count)

if __name__ == '__main__':
  main()
