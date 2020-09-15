# Q04 棒の切り分け
# n[cm]の棒を1[cm]単位に切り分けることを考えます。
# ただし、１本の棒を一度に切ることができるのは一人だけです。
# 1. n=20, m=3 のときの回数を求めてください。
# 2. n=100, m=5 のときの回数を求めてください。

# chip_list: list[int] の最後尾（一番長い棒）を半分に切り分ける
def cut_longest_chip(chip_list):
  chip = chip_list.pop()
  if chip > 1:
    results = [chip // 2, chip - chip // 2]
  else:
    results = []
  return results + chip_list

# n: int 棒の長さ m: int 切る人数 → 何回で1[cm]単位に切り分けられるかを返す
def times_for_cut(n, m):
  chip_list = [n]
  times = 0
  while chip_list[-1] > 1:
    for i in range(min(m, len(chip_list))):
      chip_list = cut_longest_chip(chip_list)
      chip_list.sort()
    times += 1
  return times

def main():
  n, m = 20, 3
  times = times_for_cut(n, m)
  print("n={}, m={}: 最短 {} 回".format(n, m, times))
  n, m = 100, 5
  times = times_for_cut(n, m)
  print("n={}, m={}: 最短 {} 回".format(n, m, times))

if __name__ == '__main__':
  main()
