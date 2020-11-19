# Q32 畳を敷きつめろ
# 畳の角が十字に交わらない（４枚の畳の角が１カ所に集まらない）敷き方で部屋に畳を敷くことを考えます。
# 問題１：縦４×横７の部屋に１４枚の畳を敷く場合、その敷き方を答えてください。
# 問題２：縦５×横６の部屋に１５枚の畳を敷く場合、その敷き方を答えてください。

# rows: int, cols: int
def init_map(rows, cols):
  imap = [[-1] * (cols + 2)]
  for _ in range(1, rows+1):
    imap.append([-1] + [0] * cols + [-1])
  imap.append([-1] * (cols + 2))
  return imap
# status: [[int]], (rows+2) * (cols+2) のリストのリスト
# 外枠は -1, 内部は畳の番号 idx が入る
def disp(status):
  def val2ch(v, line):
    if v <= 0:
      return ' '
    else:
      if line.count(v) == 2:
        return '-'
      else:
        return '|'
  rows = len(status)
  for i in range(1, rows-1):
    line = [val2ch(v, status[i]) for v in status[i][1:-1]]
    print(''.join(line))
  print('')

# status の状態から、i 行 j 列に新しい畳 idx を敷くことを考える
def set_tatami(status, i, j, idx):
  line = status[i]
  rows, cols = len(status)-2, len(line)-2
  if i > rows: # 最下段（外枠）までたどり着いたら終了
    disp(status)
  elif j > cols: # 右端（外枠）までたどり着いたら、次の行を探索
    set_tatami(status, i+1, 1, idx)
  elif line[j] > 0: # i 行 j 列にすでに畳が敷かれていたら、隣を探索
    set_tatami(status, i, j+1, idx)
  elif status[i-1][j-1] == status[i-1][j] or status[i-1][j-1] == status[i][j-1]:
    # 左上と上の畳が等しい or 左上と左の畳が等しいとき、畳は十字に交わらない
    line[j] = idx
    if line[j+1] == 0: # 横向きに畳を敷くことができる
      line[j+1] = idx
      set_tatami(status, i, j+2, idx+1)
      line[j+1] = 0
    if status[i+1][j] == 0: # 縦向きに畳を敷くことができる
      status[i+1][j] = idx
      set_tatami(status, i, j+1, idx+1)
      status[i+1][j] = 0
    line[j] = 0

