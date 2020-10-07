# Q25 オシャレな靴ひもの結び方
# スニーカーではオシャレな結び方もいくつか登場しています。そこで、いろいろな穴の通し方に注目してみます。
# ここでは、ひもを結ぶ位置は、一番上の位置に固定することにし、左右の穴を交互に使用するものとします。
# 交差する点の数が最も多くなるとき、その交点の数を求めてください。

from itertools import permutations

# holeL: 左の穴の利用順のリスト, holeR: 右の穴の利用順のリスト
# pair: (左の穴, 右の穴)
# holeL と holeR に基づいてひもを通したときに生じる pair のリストを返す
def pair_list(holeL, holeR):
  pairL = [(h, holeR[idx]) for idx, h in enumerate(holeL)]
  pairR = [(holeL[idx+1], h) for idx, h in enumerate(holeR[:-1])]
  return pairL + pairR

# pair: (左の穴, 右の穴), pair1 と pair2 が交差しているかどうかを判定する
def cross(pair1, pair2):
  if (pair1[0] - pair2[0]) * (pair1[1] - pair2[1]) < 0:
    return True
  return False

# holeL と holeR に基づいてひもを通したときに生じる交点の数を返す
def count(holeL, holeR):
  pairs = pair_list(holeL, holeR)
  num = 0
  for idx, p1 in enumerate(pairs[:-1], 1):
    num += sum([cross(p1, p2) for p2 in pairs[idx:]])
  return num

def main():
  perm_list = permutations(range(1, 6), 5)
  max_count = 0
  for p1 in perm_list:
    for p2 in perm_list:
      val = count([0] + list(p1), list(p2) + [0])
      if max_count < val:
        max_count = val
        print(max_count, [0] + list(p1), list(p2) + [0])
  print("MAX:", max_count)

if __name__ == '__main__':
  main()
