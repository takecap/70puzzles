# Q09 つりあわない男女
# 男性２０人、女性１０人が到着した場合、どこで区切っても２つのグループのいずれも
# 男女の数が異なってしまうような到着順が何通りあるかを求めてください。

# seq: ['B' or 'G']
def unbalance(seq, maxB, maxG):
  cntB, cntG = seq.count('B'), seq.count('G')
  head = cntB != cntG # 前から見て、等分割できるかを判定する
  tail = (maxB - cntB) != (maxG - cntG) # 後ろから見て、等分割できるかを判定する
  return head and tail

# tracks: { seq }
def step(tracks, max_boy, max_girl):
  results = set()
  for track in tracks:
    if track.count('B') < max_boy and unbalance(track + 'B', max_boy, max_girl):
      results.add(track + 'B')
    if track.count('G') < max_girl and unbalance(track + 'G', max_boy, max_girl):
      results.add(track + 'G')
  return results

def main():
  max_boy, max_girl = 20, 10
  tracks = {'B'}
  for i in range(28):
    tracks = step(tracks, max_boy, max_girl)
    print("{:2d}: {:7d}".format(i+2, len(tracks)))

if __name__ == '__main__':
  main()
