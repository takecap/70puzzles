# Q70 青白歌合戦

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
  memo = {g1: 0, g2: 0, g3: 0, g4: 0}
  return [g1, g2, g3, g4], masks, memo

def step(status, masks, memo, depth):
  results = []
  for num in status:
    for msk in masks:
      temp = num ^ msk
      if not (temp in memo or num & msk == 0 or num & msk == msk):
        memo[temp] = depth
        results.append(temp)
  return results

def main():
  results, masks, memo = init_status()
  cnt = 0
  while len(results) > 0:
    cnt += 1
    results = step(results, masks, memo, cnt)
    print("#{:2d}: {:6d}".format(cnt, len(results)))
  results = [res for res in memo.keys() if memo[res] == cnt - 1]
  print("Step:", cnt-1, "Results:", len(results))

if __name__ == '__main__':
  main()
