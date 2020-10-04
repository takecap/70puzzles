# Q23 ブラックジャックで大儲け？
# ブラックジャックのゲームを１回行うには、最低１枚コインが必要です。
# 勝てば２枚のコインが得られますが、負けると賭けたコインが没収されます。
# 最初に１枚だけコインを持っており、１枚ずつ賭けていったとき、
# ゲームを２４回行って手元にコインが残るような枚数の変化が何通りあるかを求めてください。

# sequence: ['W' or 'L'], coin: int, times: int, patterns: [sequence]
def search(sequence, coin, times, patterns):
  if times == 0:
    patterns.append(sequence)
  else:
    search(sequence + 'W', coin+1, times-1, patterns)
    if coin > 1:
      search(sequence + 'L', coin-1, times-1, patterns)

def main():
  patterns = []
  print('SEARCHING...')
  search('', 10, 24, patterns)
  print('TOTAL: ', len(patterns))

if __name__ == '__main__':
  main()
