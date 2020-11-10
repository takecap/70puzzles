# Q60 セルの結合パターン
# ４行４列のセルがあったとき、これを結合してできるパターンは何通りあるかを答えてください。
# また、１×１のセルがないように結合するパターンが何通りあるかを答えてください。

# ２本の区切り線のパターンを key とし、それに直行する結合パターンの集合を value とする辞書
matches = {
  (0,0): {(0,0), (1,1)},
  (0,1): {(1,1)},
  (1,0): {(1,1)},
  (1,1): {(0,0), (0,1), (1,0), (1,1)}
}

# １２本の edge の集合のすべての組合せのリストを返す
def patterns():
  def str2tpl(vals):
    return tuple(int(ch) for ch in vals)
  bins = ['{:012d}'.format(int(bin(n)[2:])) for n in range(2 ** 12)]
  return [str2tpl(vals) for vals in bins]

# ９つの格子点について、横線（rows）と縦線（cols）が matches で定められた結合パターンとなっているかを判定する
def check(rows, cols):
  for i in range(9):
    m, n = i // 3, i % 3
    r, c = m * 4 + n, n * 4 + m
    if not rows[r:r+2] in matches[cols[c:c+2]]:
      return False
  return True

# rows, cols で指定された結合パターンについて、m 行 n 列のセルが１×１になっていないかを判定する
def notUnit(rows, cols, m, n):
  if m == 0 and rows[n] == 0:
    return True
  elif (m == 1 or m == 2) and (rows[(m-1)*4+n] == 0 or rows[(m*4+n)] == 0):
    return True
  elif m == 3 and rows[2*4+n] == 0:
    return True
  if n == 0 and cols[m] == 0:
    return True
  elif (n == 1 or n == 2) and (cols[(n-1)*4+m] == 0 or cols[n*4+m] == 0):
    return True
  elif n == 3 and cols[2*4+m] == 0:
    return True
  return False

# rows, cols で指定された結合パターンについて、１×１のセルがないかを判定する
def noUnit(rows, cols):
  for m in range(4):
    for n in range(4):
      if not notUnit(rows, cols, m, n):
        return False
  return True

def main():
  all_patterns = patterns()
  results = []
  for rows in all_patterns:
    results += [(rows, cols) for cols in all_patterns if check(rows, cols)]
  print("Results:", len(results), 'cases')
  noUnits = [res for res in results if noUnit(res[0], res[1])]
  print("No Unit:", len(noUnits))

if __name__ == '__main__':
  main()
