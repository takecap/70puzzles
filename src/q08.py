# Q08 優秀な掃除ロボット
# ここでは、同じ場所を通らない掃除ロボットを考えます。このロボットは、前後左右にのみ移動することができます。
# このロボットが１２回移動するとき、考えられる移動経路のパターンが何通りあるかを求めてください。

# location: (int, int), direction: 0, 1, 2, 3 次の location: (int, int) を返す
def move(location, direction):
  if direction == 0: # 下
    return (location[0], location[1] + 1)
  elif direction == 1: # 右
    return (location[0] + 1, location[1])
  if direction == 2: # 上
    return (location[0], location[1] - 1)
  elif direction == 3: # 左
    return (location[0] - 1, location[1])

# track_list: [track], track: [(int, int)] track に次の location: (int, int) を加える
def add_one_step(track_list):
  results = []
  for track in track_list:
    for dir in range(4):
      next_loc = move(track[-1], dir)
      if not next_loc in track:
        results.append(track + [next_loc])
  return results

def main():
  times = 11
  results = [[(0, 0), (0, -1)]]
  for i in range(times):
    results = add_one_step(results)
    print("{:2d}:{:d}".format((i+2), len(results) * 4))

if __name__ == '__main__':
  main()
