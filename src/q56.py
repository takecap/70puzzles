# Q56 公平に分けられたケーキ
# ケーキを公平に切り分けることを考えます。ケーキのサイズは m * n の長方形になっており、1 * 1 の格子状の位置で、
# 直線に沿って切ることができます。一直線に切るので、一度着るごとに必ず２つに分かれます。
# ２人が交互にケーキを切っていき、切った人は小さいほうのケーキを食べます。残ったほうのケーキをもう１人が切り、
# また小さいほうを食べる、ということを繰り返します。最後の１つは切らずに、次の人が食べます。
# 16 * 12 の長方形の場合に、２人で同じ量を食べる切り方を考え、その切った部分の長さが最短になるものを求めてください。

from math import inf

# w: int, h: int, diff: 両者の取り分の差, memo: (w, h, diff) -> 切った長さの最小値
def cut(w, h, diff, memo):
  if w < h:
    w, h = h, w # 横長の長方形として考える
  if (w, h, diff) in memo:
    return memo[w, h, diff]
  if w == 1 and h == 1:
    memo[w, h, diff] = 0 if diff == 1 else inf # diff が 1 なら公平に分けられる
    return memo[w, h, diff]
  best = inf
  for i in range(1, w // 2 + 1):
    if best > h + cut(w-i, h, i * h - diff, memo):
      best = h + cut(w-i, h, i * h - diff, memo)
  for j in range(1, h // 2 + 1):
    if best > w + cut(w, h-j, j * w - diff, memo):
      best = w + cut(w, h-j, j * h - diff, memo)
  memo[w, h, diff] = best
  return memo[w, h, diff]

def main():
  rows, cols = 12, 16
  memo = {}
  print("SEARCH FOR: {:d} * {:d}".format(cols, rows))
  print("Best:", cut(cols, rows, 0, memo))

if __name__ == '__main__':
  main()
