# Q46 ソートの交換回数の最小化
# 1..n の n 個の数字について、２つの数字の交換を繰り返し、小さいほうから並べることを考えます。
# 最初の並び順によって、並べ替えるのに必要な最小の交換回数は異なっています。
# 1..7 の７つの数字からできるすべての順列において、小さいほうから順に並べるための交換を最小回数で行うとき、
# その交換回数の合計を求めてください。

from itertools import permutations

# sequence: [0..n-1], idx0, idx1: 0..n
# 数字の並びの idx0 番目と idx1 番目を交換した結果を返す
def flip(sequence, idx0, idx1):
  values = list(sequence)
  num0, num1 = sequence[idx0], sequence[idx1]
  values[idx0] = num1
  values[idx1] = num0
  return tuple(values)

# sequence を小さいほうから並べるのに必要な最小の交換回数を返す
def count(sequence, results):
  cnt = 0
  for idx0 in range(len(sequence)):
    if idx0 == sequence[idx0]:
      continue
    idx1 = sequence.index(idx0)
    sequence = flip(sequence, idx0, idx1)
    cnt += 1
    if sequence in results.keys():
      return results[sequence] + cnt
  return cnt

def main():
  num = 7
  cnt, results = 0, {}
  for seq in permutations(range(num), num):
    results[seq] = count(seq, results)
    cnt += results[seq]
  print("Num: {:d} -> {:d} times".format(num, cnt))

if __name__ == '__main__':
  main()
