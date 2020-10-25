# Q38 ７セグメントコードの反転
# ７セグメントディスプレイを使って０〰９までの１０個の数字をそれぞれ１回ずつ表示することを考えます。
# １０個の数字をすべて表示する際、点灯・消灯の切り替え回数が最も少なくなる表示順を求め、
# その切り替え回数を答えてください。

from itertools import permutations

pattern = {
  0: [True, True, True, True, True, True, False],
  1: [False, True, True, False, False, False, False],
  2: [True, True, False, True, True, False, True],
  3: [True, True, True, True, False, False, True],
  4: [False, True, True, False, False, True, True],
  5: [True, False, True, True, False, True, True],
  6: [True, False, True, True, True, True, True],
  7: [True, True, True, False, False, False, False],
  8: [True, True, True, True, True, True, True],
  9: [True, True, True, True, False, True, True]
}

def flip_counts():
  counts = {}
  for i in range(10):
    for j in range(i+1, 10):
      counts[(i, j)] = sum([bi ^ bj for bi, bj in zip(pattern[i], pattern[j])])
      counts[(j, i)] = sum([bi ^ bj for bi, bj in zip(pattern[i], pattern[j])])
  return counts
# countc[(i, j)] -> i の次に j を表示する際に生じる切り替え回数
counts = flip_counts()

# sequence: (0..9) 与えられた sequence の順に表示する際の切り替え回数の総数を返す
def count(sequence):
  cnt = 0
  for i in range(9):
    cnt += counts[sequence[i], sequence[i+1]]
  return cnt

def main():
  min_cnt = 100
  min_seq = (0, )
  for seq in permutations(range(10), 10):
    cnt = count(seq)
    if cnt < min_cnt:
      if cnt < 20:
        print(min_cnt, min_seq)
      min_cnt = cnt
      min_seq = seq
  print("MIN:", min_cnt, min_seq)

if __name__ == '__main__':
  main()
