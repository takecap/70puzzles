# Q28 クラブ活動への最適な配分
# スポーツをしたい１５０人の学生に、どんなクラブ活動を準備するか考えています。
# 各クラブに所属する部員数との関係を考え、土地を確保する必要があります。
# １５０人を超えないようにクラブ活動を選び、必要な土地の面積を最大にします。
# その面積の最大値を求めてください。

table = [
  { 'area': 11000, 'member': 40 },
  { 'area':  8000, 'member': 30 },
  { 'area':   400, 'member': 24 },
  { 'area':   800, 'member': 20 },
  { 'area':   900, 'member': 14 },
  { 'area':  1800, 'member': 16 },
  { 'area':  1000, 'member': 15 },
  { 'area':  7000, 'member': 40 },
  { 'area':   100, 'member': 10 },
  { 'area':   300, 'member': 12 }
]

def target_ids():
  results = { (): 0 } # key: (ids), value: area の dict
  for idx, club in enumerate(table):
    ids_list = list(results.keys())
    for ids in ids_list:
      members = club['member'] + results[ids] # members: (ids) に club (= table[idx]) を追加したときの部員総数
      if members <= 150:
        results[add_idx(ids, idx)] = members # members が１５０人以下なら、このクラブの組合せを results に追加する
  return results

# ids: (idx, idx,...,idx)
def add_idx(ids, idx):
  return tuple(list(ids) + [idx])

def area(ids):
  return sum([table[idx]['area'] for idx in ids])

def main():
  max_area = -1
  max_ids = {}
  ids_list = target_ids()
  for ids in ids_list:
    temp_area = area(ids)
    if max_area < temp_area:
      max_area = temp_area
      max_ids = ids
  print("MAX AREA:", max_area)
  print("TARGET:", max_ids)

if __name__ == '__main__':
  main()
