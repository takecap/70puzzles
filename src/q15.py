# Q15 階段で立ち話
# 階段を下からＡさんが上がっていくと同時に、上からＢさんが下りてきます。
# 階段は最大で３段まで飛ばして進むことができます。
# １０段の階段で移動したとき、２人が同じ段に止まるのは何通りあるかを求めてください。

# DPで解くための表 patterns: [[int]] を用意する
def init_patterns(n = 10):
  patterns = [ [0] * (n + 1) for _ in range(n // 2 + 1) ]
  patterns[0][0] = 1
  return patterns

# Ａさんが、idx 時間後に step 段目にいる場合の数を DP で求める。
# 求めた場合の数の表 patterns: [[int]] を返す
def count_patterns(n = 10):
  patterns = init_patterns(n)
  for step in range(1, n // 2 + 1):
    for idx in range(1, n + 1):
      start = max(idx - 4, 0)
      patterns[step][idx] = sum(patterns[step - 1][start:idx])
  return patterns

def count_meet_patterns(n = 10):
  num = 0
  patterns = count_patterns(n)
  for pattern in patterns:
    for step in range(1, n):
      # ＡさんとＢさんの動きは対象なので、
      # Ｂさんが step 段目にいる場合の数 = Ａさんが n - step 段目にいる場合の数
      # 両者が同じ step 段に止まる場合の数はその積で求められる
      num += pattern[step] * pattern[n - step]
    print(num)
