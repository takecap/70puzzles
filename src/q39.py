# Q39 「白」で埋めつくせ！
# ４×４のマス目が白と黒で塗り分けられています。任意のマス目について、そのマス目を選択するとき、
# その行と列の色をすべて反転（白→黒、黒→白）させる操作を行います。
# この作業を繰り返し行うことで、初期状態によらず、必ずすべて「白」に変更できます。
# このマス目を選択する回数（反転操作を行う回数）が最大になる初期状態を考え、その回数を求めてください。

target = (True, True, False, False, True, False, False, True, True, False, True, False, False, True, True, True)

def init():
  return { tuple([False] * 16) }

# status: True or False の長さ 16 のタプル
def disp(status):
  for i in range(4):
    st_list = status[i*4:(i+1)*4]
    print(['**' if st else '  ' for st in st_list])

# m 行 n 列のマス目について反転操作を行った結果を返す
def flip(status, m, n):
  st_list = list(status)
  for i in range(4):
    st_list[m * 4 + i] = not st_list[m * 4 + i]
  for j in range(4):
    st_list[j * 4 + n] = not st_list[j * 4 + n]
  st_list[m * 4 + n] = not st_list[m * 4 + n]
  return tuple(st_list)

# pre_patterns, done_patterns: status の集合
# pre_patterns 内の status について反転操作を施して、done_patterns に無い新しい status を探索する
# 得られた新しい status の集合を new_patterns として返す
def search(pre_patterns, done_patterns):
  new_patterns = set()
  exist_patterns = pre_patterns | done_patterns
  for pt in pre_patterns:
    for i in range(4):
      for j in range(4):
        status = flip(pt, i, j)
        if not status in exist_patterns:
          new_patterns.add(status)
  return new_patterns

def main():
  pre, done = init(), set()
  num, step = 1, 1
  while num < 2 ** 16:
    print("STEP:", step)
    new_patterns = search(pre, done)
    num = len(done | pre | new_patterns)
    print("ADD", len(new_patterns), "patterns, TOTAL:", num, "patterns")
    done |= pre
    pre = new_patterns
    step += 1
  print("MAX STEP:", step-1)
  for pt in pre:
    disp(pt)

if __name__ == '__main__':
  main()
