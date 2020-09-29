# Q20 受難のファサードの魔方陣
# 魔方陣を使い、下記の条件で足し算をした結果、その和が同じになる組み合わせ
# が最も多くなるような値（和）を求めてください。
# ・足し合わせるのは、縦、横、斜めに限らない
# ・足し合わせる数字の個数は４つに限らない

magic_square = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]

# num: int, combination: [int], combinations: [combination]
# 既存の数字の組み合わせの末尾に num を追加する
def add(num, combinations):
  results = [com + [num] for com in combinations]
  return results

def main():
  combinations = [[]]
  for num in magic_square:
    combinations += add(num, combinations)
  
  counts = {}
  for comb in combinations:
    val = sum(comb)
    if val in counts:
      counts[val] += 1
    else:
      counts[val] = 1
  item_sorted = sorted(counts.items(), key=lambda x: x[1], reverse=True)
  for item in item_sorted[:5]:
    print("TOTAL:{:3d}, {:5d} cases.".format(item[0], item[1]))

if __name__ == '__main__':
  main()
