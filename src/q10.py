# Q10 ルーレットの最大値
# ルーレットの数字の配置として有名なのが「ヨーロピアンスタイル」と「アメリカンスタイル」です。
# ここでは、「連続するn個の数の和」が最大になる位置を考えます。
# 2 <= n <= 36 のそれぞれの nについて、連続する n個の数の和が最大になる場合を求め、
# ヨーロピアンスタイルでの和がアメリカンスタイルでの和よりも小さくなる nがいくつあるかを求めてください。

roulette_europe  = [
  0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13,
  36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14,
  31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
]

roulette_america = [
  0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34,
  15, 3, 24, 36, 13, 1, 0, 27, 10, 25, 29, 12, 8,
  19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2
]

# roulette: [int], table: [[int]] を返す
# table[n][idx] には、roulette の idx から idx+n-1 番目の数の和が記録されている
def set_table(roulette):
  size = len(roulette)
  roulette2 = roulette * 2
  table = [[0]] * size
  table[1] = [num for num in roulette]
  for n in range(2, size):
    table[n] = [num + roulette2[idx + n -1] for idx, num in enumerate(table[n-1])]
  return table

def main():
  table_europe = set_table(roulette_europe)
  max_europe = [max(sequence) for sequence in table_europe]
  table_america = set_table(roulette_america)
  max_america = [max(sequence) for sequence in table_america]
  count = 0
  for i in range(2, 37):
    if max_europe[i] < max_america[i]:
      count += 1
      print("Num:{:2d}, EUR: {:d}, USA: {:d}".format(i, max_europe[i], max_america[i]))
  print("TOTAL: {:d} CASES".format(count))

if __name__ == '__main__':
  main()
