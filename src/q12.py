# Q012 平方根の数字
# 平方根を数字で表したときに、０〰９までの数字が最も早くすべて現れる最小の整数を求めてください。
# 整数部分を含む場合と、小数部分のみの場合のそれぞれについて求めてください。

from decimal import Decimal

# n: int の平方根を数字で表したときの数字列（整数部分含む）を返す
# n の平方根が整数になるときは、空文字列を返す
def num_digits(n):
  sqrt_str = str(Decimal(n).sqrt())
  num_digits = sqrt_str.find('.')
  if num_digits > 0:
    return sqrt_str.replace('.', '')
  else:
    return ''

# n: int の平方根を数字で表したときの数字列（小数部分のみ）を返す
# n の平方根が整数になるときは、空文字列を返す
def num_decimal(n):
  sqrt_str = str(Decimal(n).sqrt())
  num_digits = sqrt_str.find('.')
  if num_digits > 0:
    return sqrt_str[(num_digits + 1):]
  else:
    return ''

# num_str: str 対象の数の平方根を表す数字列
# limit: int 探索対象はlimit文字数まで
def count_fulfill10(num_str, limit=20):
  flag = [False] * 10 # 0〰9までの出現状況
  for i, ch in enumerate(num_str, 1):
    if not flag[int(ch)]:
      flag[int(ch)] = True
      if sum(flag) == 10:
        return i
    if i == limit:
      return i

def main():
  print("整数部分含む")
  num, best = 2, 100
  while best > 10:
    count = count_fulfill10(num_decimal(num))
    if count and count < best:
      best = count
      print("Update: {:d} {:d}".format(count, num))
    num += 1

  print("小数部分のみ")
  num, best = 2, 100
  while best > 10:
    count = count_fulfill10(num_digits(num))
    if count and count < best:
      best = count
      print("Update: {:d} {:d}".format(count, num))
    num += 1

if __name__ == '__main__':
  main()
