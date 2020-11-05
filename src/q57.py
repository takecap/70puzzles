# Q57 あみだくじの横線
# あみだくじで上と下の数字が同じになるように結ぶ横線を引くことを考えます。ただし、上と下の数字が与えられたとき、
# 最小本数の横線であみだくじを作成するものとします。上の数字「１，２，３，４，５，６，７」が与えられたとき、
# 横線の最小本数が 10 本になる下の数字の並び方が何通りあるか、その個数を求めてください。

# sequence: (int), idx: int
# sequence の idx 番と idx+1 番の数字を入替えたタプルを返す
# あみだくじの枝の追加 <=> sequence の互換
def add_edge(sequence, idx):
  size = len(sequence)
  if idx == 0:
    return (sequence[1], sequence[0]) + sequence[2:]
  elif idx < size - 2:
    return sequence[:idx] + (sequence[idx+1], sequence[idx]) + sequence[idx+2:]
  else:
    return sequence[:-2] + (sequence[-1], sequence[-2])

# results: { sequence }, num: int
# results の全ての sequence について、0..(num-1) に枝を追加して得られる sequence の集合を返す
def step(results, num):
  diff = set()
  for seq in results:
    diff |= { add_edge(seq, idx) for idx in range(num - 1) }
  return diff

def main():
  results, diff = set(), {(1,2,3,4,5,6,7)}
  size = len(results)
  for i in range(10):
    diff = step(diff, 7)
    results |= diff
    print("Edge:{:2d} Diff: {:3d} cases".format(i + 1, len(results) - size))
    size = len(results)

if __name__ == '__main__':
  main()
