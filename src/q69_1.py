# 男女平等な席替え

def patterns(cols):
  def fmt(num):
    if len(num) < cols:
      return tuple( [0] * (cols - len(num)) + [int(n) for n in num] )
    else:
      return tuple( int(n) for n in num )
  return [fmt(bin(n)[2:]) for n in range(2 ** cols)]

def check(r1, r2, r3):
  size = len(r1)
  r0 = (-1,) * (size + 2)
  rows = [r0, (-1,) + r1 + (-1,), (-1,) + r2 + (-1,), (-1,) + r3 + (-1,)]
  for i in range(1, 3):
    for idx, sex in enumerate(rows[i][1:-1], 1):
      neighbors = [rows[i-1][idx], rows[i][idx-1], rows[i][idx+1], rows[i+1][idx]]
      opposite = 1 - sex
      if not opposite in neighbors:
        return False
  return True

def next_rows(cols):
  pts = patterns(cols)
  oks = {}
  for r1 in pts:
    for r2 in pts:
      oks[r1, r2] = [r3 for r3 in pts if check(r1, r2, r3)]
  return oks

def finish(r1, r2):
  size = len(r1)
  s1, s2 = (-1,) + r1 + (-1,), (-1,) + r2 + (-1,)
  for i in range(1, size+1):
    neighbors = [s2[i-1], s2[i+1], s1[i]]
    opposite = 1 - s2[i]
    if not opposite in neighbors:
      return False
  return True

def search(r1, r2, remain, mens, rows, nexts, memo):
  if (r1, r2, remain, mens) in memo:
    return memo[r1, r2, remain, mens]
  if remain == 0:
    size = len(r1) * rows
    memo[r1, r2, remain, mens] = 1 if finish(r1, r2) and mens == size // 2 else 0
    return memo[r1, r2, remain, mens]
  else:
    cnt = 0
    for r in nexts[r1, r2]:
      cnt += search(r2, r, remain-1, mens+r.count(1), rows, nexts, memo)
    return cnt
