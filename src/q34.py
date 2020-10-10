# Q34 飛車と角の利き
# 飛車と角を盤面に配置することをすべての位置について考え、２つのコマの利きに入るマス目の合計を求めてください。

# ban の初期状態を返す。(1,1) 〰 (9,9) は 0、外枠には -1 をセットする
def init_ban():
  ban = [[-1] + [0] * 9 + [-1] for _ in range(11)]
  ban[0] = [-1] * 11
  ban[-1] = [-1] * 11
  return ban

# masu: (m, n), direction: (±1, ±1), num: int
def search(ban, masu, direction):
  value = ban[masu[0]][masu[1]]
  if value == -1: # 探索対象のマスが外枠 or 飛車角のマスの場合
    return 0
  next_masu = (masu[0] + direction[0], masu[1] + direction[1])
  if value == 1: # 探索対象のマスがすでにカウントされているマス目の場合
    return search(ban, next_masu, direction)
  else: # 探索対象のマスがまだカウントされていない場合
    ban[masu[0]][masu[1]] = 1
    return search(ban, next_masu, direction) + 1

def count_hisha(ban, m, n):
  val = 0
  for i in range(-1, 2, 2): # i = -1, 1
    val += search(ban, (m+i, n), (i, 0)) + search(ban, (m, n+i), (0, i))
  return val

def count_kaku(ban, m, n):
  val = 0
  for i in range(-1, 2, 2): # i = -1, 1
    for j in range(-1, 2, 2): # j = -1, 1
      val += search(ban, (m+i, n+j), (i, j))
  return val

# hisha: (m1, n1), kaku: (m2, n2)
def count(hisha, kaku):
  ban = init_ban()
  ban[hisha[0]][hisha[1]] = -1
  ban[kaku[0]][kaku[1]] = -1
  return count_hisha(ban, hisha[0], hisha[1]) + count_kaku(ban, kaku[0], kaku[1])

def main():
  val = 0
  for m1 in range(1, 10):
    for n1 in range(1, 10):
      for m2 in range(1, 10):
        for n2 in range(1, 10):
          if (m1, n1) == (m2, n2):
            continue
          val += count((m1,n1), (m2,n2))
    print("hisha @ col{:d}. TOTAL:{:6d} count".format(m1, val))

if __name__ == '__main__':
  main()
