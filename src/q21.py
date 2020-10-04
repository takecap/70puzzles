# Q21 排他的論理和で作る三角形
# 「パスカルの三角形」は「右上の数と左上の数の和」を配置していますが、ここでは単純な「和」ではなく、
# 「排他的論理和」を使うことを考えます。上から順番に配置していったとき、２０１４番目の「０」
# 出力されるのは何段目になるかを求めてください。

def next_column(column):
  return [bl1 ^ bl2 for bl1, bl2 in zip([False] + column, column + [False])]

def main():
  column = [True]
  count = 0
  num = 2
  while count < 2015:
    column = next_column(column)
    count += column.count(False)
    if count > 2000:
      print("STEP{:3d}, COUNT {:d}".format(num, count))
    num += 1

if __name__ == '__main__':
  main()
