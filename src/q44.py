# Q44 グラスの水を半分に
# すべてサイズが違うＡ，Ｂ，Ｃの３つのグラスがあります。
# Ａに水が満たされていて、ＢとＣが空であるところから始め、１つのグラスから他の２つのグラスに水を移すことを繰り返します。
# 移すときには一方が空になるか、一方が満タンになるかのどちらかです。これを繰り返すことで、Ａに残る水の量を
# 「最初の半分」にすることを考えます。Ａの容量を１０以上１００以下の偶数とするとき、移動によってＡに残る水の量を
# 最初の半分にできる（Ａ，Ｂ，Ｃ）の組の個数を答えてください。

from math import gcd

# volume: 0..capacity, status: (volume0, volume1, volume2)
# fr, to: 0 or 1 or 2
def move(status, capacities, fr, to):
  results = [st for st in status]
  if fr == to or status[fr] == 0 or capacities[to] == status[to]: # 移動が生じない
    return status
  diff = capacities[to] - status[to] # 移動可能な水量
  if status[fr] > diff: # 移動元の水量が多い → 移動先を満タンにする
    results[fr] = status[fr] - diff
    results[to] = capacities[to]
    return tuple(results)
  else: # 移動可能な水量が多い → 移動元を空にする
    results[fr] = 0
    results[to] = status[to] + status[fr]
    return tuple(results)

# achieved: { status }, 探索済の status の集合
# 現在の水の量から１回の移動で達成できる新しい status の集合を返す
def step(status, capacities, achieved):
  patterns = set()
  for i in range(3):
    for j in range(3):
      new_status = move(status, capacities, i, j)
      if not new_status in achieved:
        patterns.add(new_status)
  return patterns

# (capA, capB, capC) の組でＡの水の量を半分にできるかどうかを判定する
def can_half(capA, capB, capC):
  achieved = { (capA, 0, 0) } # 達成済の status の集合
  checking = { (capA, 0, 0) } # 探索起点となる状態の集合
  diff = set() # 探索によって新たに達成した status の集合
  while True:
    for status in checking: # 前のステップで追加された status から、新たに達成できる status を探索する
      diff |= step(status, (capA, capB, capC), achieved | diff)
    for status in diff: # 新たに追加された status のうち、条件を満たすものがあれば探索は終了
      if status[0] == capA // 2:
        return True
    achieved |= diff # 達成済の status の集合を更新
    if len(diff) == 0: # 新たに達成できる status が見つからなければ、探索は失敗
      return False
    checking, diff = diff, set()

# n: グラスＡの容量, Ａの水の量を n/2 にできる（Ａ，Ｂ，Ｃ）の組の個数を返す
def search(n):
  count = 0
  for i in range(1, n // 2, 2):
    if gcd(n-i, i) == 1 and can_half(n, n-i, i):
      count += 1
  return count

def main():
  count = 0
  for i in range(10, 102, 2): # 10, 12,...,100
    count += search(i)
  print(count)

if __name__ == '__main__':
  main()
