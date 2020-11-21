# Q58 最速の連絡網
# 連絡網を使い、矢印の向きにしたがって、前の人から後ろの人に順番に電話します。正しく伝わったか確認するため、
# 最期の人は先頭の人に連絡することにします。なお、同時に１人が複数の人と話すことはできません。
# 先生が１人、生徒が１４人のクラスがあり、電話をするのに各１分かかるとします。全員に伝わったことを
# 先生が把握するまでにかかる時間を最も短くするとき、その時間を求めてください。

# status: [#yet, #got, #done, #teacher]
def step(status):
  results = set()
  for d in range(status[2] + 1): # done -> yet への連絡の数
    for s in range(status[1] + 1): # got -> yet への連絡の数
      n = status[0] - d - s # 連絡後の yet の人数
      if n >= 0:
        results.add((n, status[1]+d, status[2]+s, status[3]))
      if n > 0: # 先生から yet への連絡を行う
        results.add((n-1, status[1]+d, status[2]+s+1, status[3]+1))
      if status[1] > 0 and n+1 >= 0:
        # got -> yet へ s-1 人、先生へ１人が連絡する
        results.add((n+1, status[1]+d-1, status[2]+s, status[3]+1))
  return results

def main():
  n = 14
  st = (n, 0, 0, 0)
  results, temp, fins, cnt = set(), {st}, [], 0
  while len(fins) == 0:
    results |= temp
    temp = set()
    for st in results:
      temp |= step(st)
    cnt += 1
    fins = [st for st in temp if st[2] == n]
  print("Done", cnt, "times")
  for st in fins:
    print(st)

if __name__ == '__main__':
  main()
