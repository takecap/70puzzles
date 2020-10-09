# Q31 最短経路の計算
# 一辺の長さが 1cmの正方形のマス目で区切られています。この境界上を最短距離で往復することを考えます。
# このとき、往路で通った道は袋では通ることができないものとします。
# 一辺の長さが 6cmの正方形の場合、最短経路がいくつあるか求めてください。

# n: int, (0, 0) → (n, n) への経路のリストを返す
def init_patterns(n):
  patterns = [[[]] * (n+1) for _ in range(n+1)]
  patterns[0][0] = [[(0, 0)]]
  for i in range(1, n+1):
    patterns[0][i] = [ p + [(0, i)] for p in patterns[0][i-1]]
  for j in range(1, n+1):
    patterns[j][0] = [ p + [(j, 0)] for p in patterns[j-1][0]]
  
  for i in range(1, n+1):
    for j in range(1, n+1):
      patterns[i][j] = [ p + [(i, j)] for p in patterns[i-1][j] + patterns[i][j-1]]
  
  return patterns[n][n]

# node: (i, j), pattern: [node], (0, 0) → (n, n) への経路を受け取り
# edge: ((i1, j1), (i2, j2)), track: { edge } を返す
def track(pattern):
  combinations = zip(pattern[:-1], pattern[1:])
  return set([(node1, node2) for node1, node2 in combinations])

def main():
  patterns = init_patterns(6)
  num = 0
  for pt1 in patterns:
    set1 = track(pt1)
    for pt2 in patterns:
      set2 = track(pt2)
      if set1 & set2 == set(): # edge を共有しない pattern を数える
        num += 1
  print("TRACKS:", num)

if __name__ == '__main__':
  main()
