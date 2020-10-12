# Q36 「０」と「７」の回文数
# 任意の正の整数 n について、「０と７の数字のみ」で構成される n の正の倍数が存在することが知られています。
# ここでは、「０と７の数字のみ」で構成される n の正の倍数の中で最小の数を求め、それが回文数になっているものを考えます。
# １ 〰 ５０までの n について、条件を満たすものを、例に挙げた「１３」以外ですべて求めてください。

# num: int 「０と７の数字のみ」で構成されているかを判定する
def composed70(num):
  num_str = str(num)
  return len(num_str) == num_str.count('7') + num_str.count('0')

# num: int 「０と７の数字のみ」で構成される num の正の倍数の中で最小の数を探索する
# value: 求めた倍数, multiple: value = num * multiple を満たす (value, multiple) を返す
# ただし、求めた倍数が回文数になっていない場合はタプルの先頭を -1 として返す
def search(num):
  digit1 = num % 10
  if digit1 % 2 == 0 or digit1 % 5 == 0:
    return (-1, -1)
  multiple_table = { 1: 7, 3: 9, 7: 1, 9: 3 }
  multiple = multiple_table[digit1]
  while True:
    value = num * multiple
    if composed70(value):
      if str(value) == str(value)[::-1]:
        return (value, multiple)
      else:
        return (-1, multiple)
    multiple += 10

def main():
  count = 0
  for i in range(1, 51):
    if i == 13:
      continue

    result = search(i)
    if result[0] > 0:
      print("{:2d} * {:d} = {:d}".format(i, result[1], result[0]))
      count += 1
  print("TOTAL: {:d} cases".format(count))

if __name__ == '__main__':
  main()
