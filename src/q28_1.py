# Q28 クラブ活動への最適な配分

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

# students: int、スポーツをしたい学生の上限値
# 動的計画法で土地の面積の最大値を探索する
def search(students):
  results = [[0] * (students+1) for _ in range(len(table) + 1)]
  for idx, club in enumerate(table, 1):
#    print(idx, club)
    area, member = club['area'], club['member']
    for num in range(1, students+1):
      if num < member or results[idx-1][num] > results[idx-1][num-member] + area:
        results[idx][num] = results[idx-1][num]
      else:
        results[idx][num] = results[idx-1][num-member] + area
  return results

def main():
  results = search(150)
  print("MAX:", results[-1][-1])

if __name__ == '__main__':
  main()
