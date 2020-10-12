# Q37 サイコロの反転
# ６個のサイコロを１列に並べることを考えます。先頭のサイコロの目が n のとき、
# 最初の n 個のサイコロを裏返して後ろに付けることにします。
# この操作を繰り返すと、同じ目が何度も現れてループします。
# このとき、最初の目に戻らない数がいくつあるか、その個数を求めてください。

from itertools import product

# sequence: ６個のサイコロの目のリスト
# 受け取った sequence に対して問題の操作を行った結果を返す
def step(sequence):
  idx = sequence[0]
  flipped = [(7 - n) for n in sequence[:idx]]
  return sequence[idx:] + flipped

# sequence: ６個のサイコロの目のリスト（初期配置）
# false_sequences: 既知の「最初の目に戻らない配置」の集合
# true_sequences: 既知の「最初の目に戻る配置」の集合
def check(sequence, false_sequences, true_sequences):
  achieved = [tuple(sequence)] # 操作を繰り返して得られる sequence を保存するリスト
  next_sequence = [num for num in sequence] # 初期配置をコピー
  while True:
    next_sequence = step(next_sequence)
    if next_sequence == sequence: # 初期配置に戻る → achieved の配置は、全て初期配置に戻る
      true_sequences |= set(achieved)
      return
    elif tuple(next_sequence) in achieved: # 初期配置以外の配置に戻る
      idx = achieved.index(tuple(next_sequence))
      false_sequences |= set(achieved[:idx]) # next_sequence より前の sequence は「最初の目に戻らない配置」
      true_sequences |= set(achieved[idx:]) # next_sequence 以降の sequence は「最初の目に戻る配置」
      return
    achieved.append(tuple(next_sequence))
  for seq in achieved:
    print(seq)

def main():
  false_sequences, true_sequences = set(), set()
  n1 = 1
  for sequence in product(range(1,7), repeat=6):
    if sequence in false_sequences | true_sequences:
      continue
    if n1 != sequence[0]:
      print("#{:d} DONE. FOUND: {:d}".format(n1, len(false_sequences)))
      n1 = sequence[0]
    check(list(sequence), false_sequences, true_sequences)
  print("#{:d} DONE. FOUND: {:5d} cases".format(n1, len(false_sequences)))

if __name__ == '__main__':
  main()
