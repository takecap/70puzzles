# Q24 完璧に撃ち抜くストラックアウト
# 「ストラックアウト」の９枚の的を抜く順番を考えます。
# ただし、周囲にフレームがある５番の的以外では、隣り合う的が存在する場合に２枚抜きすることができます。
# ９枚の的を抜く順番が何通りあるかを求めてください。投げたボールは必ずいずれかの的に当たるものとします。

targets = [
  {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9},
  {1, 2}, {1, 4}, {2, 3}, {3, 6}, {4, 7}, {6, 9}, {7, 8}, {8, 9}
]

# tgt: {int}, candidates: {tgt}
def cut(tgt, candidates):
  return [cd for cd in candidates if cd & tgt == set()]

# seq: [tgt], candidates: {tgt}, results: [seq]
def search(seq, candidates, results):
  if len(candidates) == 0:
    results.append(seq)
  else:
    for tgt in candidates:
      next_candidates = cut(tgt, candidates)
      search(seq + [tgt], next_candidates, results)

def main():
  results = []
  search([], targets, results)
  print("PATTERNS:", len(results))

if __name__ == '__main__':
  main()
