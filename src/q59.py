# Q59 ハンカチ落としの総走行距離
# ハンカチ落としでは、鬼以外の人が円になって座ったあと、鬼が円の外を走ります。鬼が誰かの後ろでハンカチを落とすと、
# 落とされた人は鬼が一周してくるまでの間に気づき、鬼を追いかける必要があります。今回は、全員が同じ速さで走るため、
# 鬼が追い付かれることはないものとし、また、落とされた人は鬼が一周回ってくるまでに必ず気づくものとします。
# このゲームを行い、円に並んでいる人の並び順を「最初の並び順の逆にする」ことを考えます。
# １〰８の番号が付いた８人が座っているところに、「０」の鬼が入ったとき、並び順が逆になる場合の
# 総走行距離が「最短」になる場合を考え、その走行距離を答えてください。

# status: 'seq'-> 現在の並び順, 'oni'-> 現在の鬼, 'start'-> 鬼が座っていた位置, 'dist'-> これまでの総走行距離
def init(num):
  start = [i for i in range(1, num+1)]
  status = {'seq': start, 'oni': 0, 'start': 0, 'dist': 0}
  goal = [1] + [i for i in range(num, 1, -1)]
  return status, goal

# seq: [int], goal: [int]
# 変更すべき番号のリストを返す
def candidates(seq, goal):
  size = len(seq)
  idxes = [idx for idx in range(size) if seq[idx] != goal[idx]]
  return idxes

# status の状態で drop 番目にハンカチを落とした後の新しい status を返す
def step(status, drop):
  next_seq = [i for i in status['seq']]
  next_seq[drop] = status['oni']
  next_oni = status['seq'][drop]
  dist = status['dist'] + drop - status['start'] + len(next_seq)
  if drop < status['start']:
    dist += len(next_seq)
  return {'seq': next_seq, 'oni': next_oni, 'start': drop, 'dist': dist}

def search(num):
  status, goal = init(num)
  st_list, new_list = [], [status]
  results = []
  while len(results) == 0:
    st_list = new_list
    new_list = []
    for st in st_list:
      new_list += [step(st, drop) for drop in candidates(st['seq'], goal)]
    results += [st for st in new_list if st['seq'] == goal]
    new_list = [st for st in new_list if st['seq'] != goal]
  min_dist = 1000
  for st in results:
    if min_dist > st['dist']:
      min_dist = st['dist']
  return min_dist

def main():
  num = 8
  print("size:", num)
  min_dist = search(num)
  print("min dist", min_dist)

if __name__ == '__main__':
  main()

def search2(num):
  status, goal = init(num)
  st_list, new_list = [], [status]
  results, memo = [], {}
  while len(results) == 0:
    st_list = new_list
    new_list, temp = [], []
    for st in st_list:
      temp += [step(st, drop) for drop in candidates(st['seq'], goal)]
    for st in temp:
      if st['seq'] == goal:
        results.append(st)
      if not tuple(st['seq']) in memo:
        new_list.append(st)
      elif memo[tuple(st['seq'])] > st['dist']:
        memo[tuple(st['seq'])] = st['dist']
        new_list.append()
  min_dist = 1000
  for st in results:
    if min_dist > st['dist']:
      min_dist = st['dist']
  return min_dist
