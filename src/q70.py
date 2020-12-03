# Q70 青白歌合戦
# バラバラに分かれているとカウントが大変ですので、ここでは勝ち負けがだれでも一目でわかるように、カウントされる側の人に
# 移動してもらうことにします（青と白が同じ人数いる場合、境界線が縦か横に一直線になるようにします）。ただし、一度に移動できるのは
# ２人だけで、縦か横に隣り合う人だけが交代できます。6 * 4 の２４人で１２人ずつに分かれる場合、その移動する回数が最大のものを探し、
# 移動パターンが何通りあるかを求めてください。

def disp(num):
  status = bin(num)[2:]
  status = '0' * (24 - len(status)) + status
  for i in range(6):
    print(status[(4*i):(4*(i+1))])

def init_status():
  all = (1 << 24) - 1
  g1 = (1 << 12) - 1
  g2 = g1 ^ all
  g3 = int('1' + '0001' * 5, 2) * 3
  g4 = g3 ^ all

  masks = []
  for i in range(24):
    if i % 4 < 3:
      masks.append(3 << i)
    if i < 20:
      masks.append(17 << i)
  return [g1, g2, g3, g4], masks

# status: [int], memo はパターンを表す int を key, goal からの移動回数を val とする辞書
# status から１回の移動で得られる新しい状態のリストを返す
def step(status, masks, memo):
  results = []
  for num in status:
    for msk in masks:
      if num & msk != 0 and num & msk != msk and not (num ^ msk in  memo):
        results.append(num ^ msk)
  return results

def main():
  results, masks = init_status()
  memo, cnt = {}, 0
  for goal in results:
    memo[goal] = cnt
  while len(results) > 0:
    cnt += 1
    results = step(results, masks, memo)
    for res in results:
      memo[res] = cnt
    print(cnt, len(results))
  results = [res for res in memo.keys() if memo[res] == cnt - 1]
  print("Step:", cnt-1, "Results:", len(results))

if __name__ == '__main__':
  main()
