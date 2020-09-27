# Q17 ３０人３１脚に挑戦！
# 「３０人３１脚」を有利に戦うための並び方を考えます。女の子が続いて並ぶと体力的に不利なので、
# 女の子は隣り合わないようにします（男の子は何人並んでもよいものとします）。
# ３０人を１列に並べるとき、その並べ方が何通りあるかを求めてください。

# pattern: ['B' or 'G'], prev_patterns: [pattern]
# 男女の並び方のパターンに対して、末尾に 'B' or 'G' を追加する
def append_patterns(prev_patterns):
  results = []
  for pattern in prev_patterns:
    if pattern[0] == 'B':
      results.append(['B'] + pattern)
      results.append(['G'] + pattern)
    else:
      results.append(['B'] + pattern)
  return results

def main():
  patterns = [['B'], ['G']]
  for num in range(29):
    patterns = append_patterns(patterns)
    print("{:2d}: {:d}".format(num+2, len(patterns)))

if __name__ == '__main__':
  main()
