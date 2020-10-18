# Q43 シャッフルで逆順
# ここでは、2n 枚のカードがあったとき、そのうち n 枚のカードをまとめて抜き出し、その他のカードの上に重ねる動作を繰り返します。
# これを繰り返して、最初の並びの逆順になるまで繰り返すことにします。
# n = 5 のとき、１０枚のカードを逆順にするために必要な最小の回数を答えてください。

# seq: 2n 枚のカードの並び, idx: シャッフルの基点になるカードの位置
# idx 枚目を基点に seq をシャッフルした結果を返す
def step(seq, idx, n):
  return seq[idx:idx+n] + seq[:idx] + seq[idx+n:]

# idx 枚目を基点にシャッフルした結果が seq になるようなカードの並びを返す
def back(seq, idx, n):
  return seq[n:n+idx] + seq[:n] + seq[n+idx:]

# seq をシャッフルして得られるカードの並びの集合を返す
def step_set(seq, n):
  return set([step(seq, idx, n) for idx in range(1, n+1)])

# シャッフルして seq になるようなカードの並びの集合を返す
def back_set(seq, n):
  return set([back(seq, idx, n) for idx in range(1, n+1)])

def main():
  n = 5
  start = tuple(range(1, 2*n+1)) # 1, 2,..., 2*n
  goal = tuple(range(2*n, 0, -1)) # 2*n, 2*n-1,..., 1
  dForwards, dBacks = {start}, {goal}
  times = 0
  while True:
    # dForwards: start からシャッフルを繰り返して得られるカードの並びの集合
    # dBacks: goal になるようなカードの並びの集合
    if dForwards & dBacks != set():
      print("n =", n, "TIMES:", times)
      break
    new_sets = set()
    if times % 2 == 0:
      for seq in dBacks:
        new_sets |= back_set(seq, n)
      dBacks = new_sets
    else:
      for seq in dForwards:
        new_sets |= step_set(seq, n)
      dForwards = new_sets
    times += 1

if __name__ == '__main__':
  main()
