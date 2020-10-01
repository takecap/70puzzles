# Q33 百人一首の達人
# 「村雨の　霧もまだひぬ　まきの葉に　霧たちのぼる　秋の夕ぐれ」の句であれば、
# 上の句は１文字、下の句も１文字の合計２文字で一意に識別することができます。
# すべての句（１００句）を一意に識別するのに必要な最小の文字数を求めてください。

import csv

# 百人一首のデータを読み込む
with open('data/q33.csv', encoding='utf-8') as f:
  reader = csv.reader(f)
  data = [row for row in reader]

# ３列が「上の句かな」、４列が「下の句かな」のデータ
kaminoku = [d[3] for d in data]
simonoku = [d[4] for d in data]

# ku: str 上の句（or 下の句）, candidates: [ku] 上の句（or 下の句）のリスト
def kimari(ku, candidates):
  num = 0
  while len(candidates):
    num += 1
    # 頭の num 文字まで共通の句を集める
    candidates = [kami for kami in candidates if kami[:num] == ku[:num]]
  return ku[:num]

def main():
  count = 0
  results = {}
  for i in range(1, 101):
    kami = kaminoku[i]
    kimari_k = kimari(kami, kaminoku[:i] + kaminoku[i+1:])
    simo = simonoku[i]
    kimari_s = kimari(simo, simonoku[:i] + simonoku[i+1:])
    results[i] = (kimari_k, kimari_s)
    count += len(kimari_k) + len(kimari_s)
  print("TOTAL:", count)

if __name__ == '__main__':
  main()
