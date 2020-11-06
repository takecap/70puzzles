# Q53 いたずらされたお菓子
# ４種類のお菓子が１個ずつあった場合、どのお菓子も包み紙と中身が不一致になるのは何通りあるかを求めてください。

from copy import deepcopy

# candy: お菓子の種類を表す idx, variety: お菓子の種類の数, num: お菓子が何個ずつあるか, status: 長さが variety * num のタプル
# candy に使える包み紙がまだ残っているお菓子の種類のリストを返す
def candidates(candy, status, variety, num):
  def has_margin(cd, st, num):
    return st.count(cd) < num
  return [idx for idx in range(variety) if has_margin(idx, status, num) and idx != candy]

# idx 番目の status を candy にアップデートする
def update(status, idx, candy):
  result = [num for num in status]
  result[idx] = candy
  return tuple(result)

# results: {status: int}, status の状態から、題意を満たす包み方が何通りあるかを記録した dict
def search(status, variety, num, results):
  if status in results:
    return results[status]
  if min(status) > -1:
    results[status] = 1
    return 1
  idx = status.index(-1)
  candy = idx // num
  indexes, counts = candidates(candy, status, variety, num), 0
  for cidx in indexes:
    new_status = update(status, idx, cidx)
    results[new_status] = search(new_status, variety, num, results)
    counts += results[new_status]
  return counts

def main():
  var, num = 4, 1
  status, results = (-1, ) * var * num, {}
  print("Variety:", var, "Num:", num)
  cnt = search(status, var, num, results)
  print("Count:", cnt)

if __name__ == '__main__':
  main()
