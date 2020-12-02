# Q59 ハンカチ落としの総走行距離

# status: 'seq'-> 現在の並び順, 'oni'-> 現在の鬼, 'start'-> 鬼が座っていた位置, 'dist'-> これまでの総走行距離
# size: 円に並んでいる人数, 'log': 鬼を務めた人の番号
def init(num):
  start = [0] + [i for i in range(2, num+1)]
  status = {'seq': start, 'oni': 1, 'start': 0, 'dist': num, 'size': num, 'log': '0'}
  goal = [1] + [i for i in range(num, 1, -1)]
  return status, [goal[i:] + goal[:i] for i in range(num)]

# status の状態で oni が diff 番目の位置にハンカチを落とした後の新しい status を返す
def step(status, diff):
  drop = (status['start'] + diff) % status['size']
  next_seq = [i for i in status['seq']]
  next_seq[drop] = status['oni']
  next_oni = status['seq'][drop]
  dist = status['dist'] + diff + status['size']
  log = status['log'] + str(status['oni'])
  return {'seq': next_seq, 'oni': next_oni, 'start': drop, 'dist': dist, 'size': status['size'], 'log': log}

def search(status, goals, results):
  if status['seq'] in goals:
    print(status['log'], status['dist'])
    results[status['log']] = status['dist']
    if status['dist'] < results['best']:
      results['best'] = status['dist']
    return
  for diff in range(1, status['size']):
    if status['dist'] + diff + status['size'] < results['best']:
      st = step(status, diff)
      search(st, goals, results)

def main():
  size = 8
  status, goals = init(size)
  results = {'best': 100}
  print('Size:', size, 'Best:', results['best'])
  search(status, goals, results)

if __name__ == '__main__':
  main()
