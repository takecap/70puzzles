# Q61 同じ大きさに分割
# 縦 m マス、横 n マスの長方形があります。これを同じ大きさの２つの領域に分割することを考えます。
# ただし、それぞれの領域（同じ色の領域）はすべて縦・横でつながっている（隣り合っている）ものとします。
# ２つの領域の形については同じでなくてもよく、大きさだけが同じであるものとします。
# m = 5, n = 4 のとき、何通りの分割方法があるか、その個数を求めてください
# （分割する線の位置を決めるものとし、色が逆のパターンは１つとカウントします）。

def nto01(n, d):
  b = bin(n)[2:]
  if len(b) < d:
    return '0' * (d - len(b)) + b
  else:
    return b

# num: m * n, 長さが num で、０と１が半分ずつの数字列のリストを返す
# 色が逆のパターンを数えないように、先頭は１に固定している
def candidates(num):
  num_list = ['1' + nto01(n, num-1) for n in range(2 ** (num-1))]
  return [n for n in num_list if n.count('1') == num // 2]

# seq: ['0' or '1'], idx: int, rows: int, cols: int
# ０と１の数字列の中で、idx 番目と直接つながっている同じ色のマスの idx の集合を返す
def touch(seq, idx, rows, cols):
  i, j = idx // cols, idx % cols
  val, idx_set = seq[idx], set()
  if i == 0:
    idx_set.add(idx+cols)
  elif i == rows - 1:
    idx_set.add(idx-cols)
  else:
    idx_set |= {idx+cols, idx-cols}
  if j == 0:
    idx_set.add(idx+1)
  elif j == cols - 1:
    idx_set.add(idx-1)
  else:
    idx_set |= {idx+1, idx-1}
  return set(idx for idx in idx_set if seq[idx] == val)

# ０と１の数字列の中で、idx 番目のマスからたどれる同じ色のマスの集合を返す
def connection(seq, idx, rows, cols):
  result, diff = { idx }, touch(seq, idx, rows, cols)
  while diff != set():
    result |= diff
    temp = set()
    for i in diff:
      temp |= touch(seq, i, rows, cols)
    diff = temp - result
  return result

def main():
  rows, cols, cnt = 4, 5, 0
  cds = candidates(rows * cols)
  print("Searching:", len(cds))
  for cd in cds:
    idx = cd.index('0')
    if len(connection(cd, idx, rows, cols)) != 10:
      continue
    idx = cd.index('1')
    if len(connection(cd, idx, rows, cols)) != 10:
      continue
    cnt += 1
  print("Result:", cnt)

if __name__ == '__main__':
  main()

def disp(num, rows, cols):
  for i in range(rows):
    print(num[i*cols:(i+1)*cols])
