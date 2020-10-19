# Q27 右折を禁止されても大丈夫？
# 直進か左折のみで目的地に到達する方法を考えてみます。格子状の道路で、直進か左折のみ、
# かつ同じ道路を通らずに移動しなければならないとします。このとき、交差しても構いません。
# ６マス×４マスの場合、何通りの道順があるかを求めてください。

# loc: (x, y), dir: 0..3
def next_location(loc, dir):
  if dir == 0: # 上
    return (loc[0], loc[1] + 1)
  elif dir == 1: # 左
    return (loc[0] - 1, loc[1])
  elif dir == 2: # 下
    return (loc[0], loc[1] - 1)
  else: # 右
    return (loc[0] + 1, loc[1])

# edges: {(x0, y0, x1, y1)}
def can_go(loc, dir, edges, rows, cols):
  next_loc = next_location(loc, dir)
  if not ((0 <= next_loc[0] < cols) and (0 <= next_loc[1] < rows)):
    return False
  if loc + next_loc in edges:
    return False
  return True

# sequence: [(loc, dir)], track: {sequence, edges}
# sequence を現在状態として、１歩進んで得られる track のリストを返す
def move(track, rows, cols):
  results = []
  sequence = track['sequence']
  edges = track['edges']
  loc, dir = sequence[-1][0], sequence[-1][1]
  if can_go(loc, dir, edges, rows, cols):
    next_loc = next_location(loc, dir)
    next_state = (next_loc, dir)
    results.append({'sequence': sequence + [next_state], 'edges': edges | {loc + next_loc, next_loc + loc}})
  dir = (dir + 1) % 4
  if can_go(loc, dir, edges, rows, cols):
    next_loc = next_location(loc, dir)
    next_state = (next_loc, dir)
    results.append({'sequence': sequence + [next_state], 'edges': edges | {loc + next_loc, next_loc + loc}})
  return results

def main():
  rows, cols = 4, 6
  start = ((0, 0), 3)
  track_list = [{ 'sequence': [start], 'edges': set() }]
  complete_list = []
  step = 0
  while len(track_list) > 0:
    new_list = []
    for track in track_list:
      new_list += move(track, rows+1, cols+1)
      track_list = [track for track in new_list if track['sequence'][-1][0] != (cols, rows)]
    complete_list += [track for track in new_list if track['sequence'][-1][0] == (cols, rows)]
    step += 1
    print("Step:{:3d}, Searching:{:5d} cases".format(step, len(track_list)))
  print("TOTAL", len(complete_list), "cases")

if __name__ == '__main__':
  main()
