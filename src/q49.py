# Q49 反転で作る互い違い
# 円形に並んだ 2n 枚のカードがあります。最初は白い n 枚のカードと黒い n 枚のカードがそれぞれ連続して並んでいます。
# ここから、連続する 3 枚のカードを異なる色に入れ替える操作を繰り返して、白と黒が交互に並ぶようにします。
# n = 8 のとき、白と黒を交互に並べられる最短の回数を求めてください。

# sequence: (bool), idx: int
# sequence の idx..idx+2 の値を反転する
def flip(sequence, idx):
  result, size = [bl for bl in sequence], len(sequence)
  for i in range(3):
    result[(idx+i) % size] = not result[(idx+i) % size]
  return tuple(result)

# seq_set: { seq }
# seq_set 内の seq を flip して得られる seq の集合を返す
def step(seq_set, num):
  results = set()
  for seq in seq_set:
    results |= set( flip(seq, idx) for idx in range(num * 2) )
  return results

def main():
  num = 8
  start = tuple( [True] * num + [False] * num )
  goal = tuple( [True, False] * num )
  steps, backs = set(), set()
  diffs, diffb, count = {start}, {goal}, 0
  while count < 100:
    if diffs & diffb:
      print("Step:", count)
      return
    steps |= diffs
    diffs = step(diffs, num) - diffs
    count += 1
    if diffs & diffb:
      print("Step:", count)
      return
    backs |= diffb
    diffb = step(diffb, num) - diffb
    count += 1
  print("Not Match...", count)

if __name__ == '__main__':
  main()
