# Q11 フィボナッチ数列
# フィボナッチ数列のうち、各桁の数字を足した数で割り切れる数を、以下の例に続けて
# 小さいほうから５個求めてください。

from functools import reduce

# n: int, fib_list: list[int] → fib_list[n]の値を更新し、各桁の数字の和を返す
def fib_digit(n,  fib_list):
  val = fib_list[n - 2] + fib_list[n - 1]
  fib_list[n] = val
  return reduce(lambda accum, ch: accum + int(ch), str(val), 0)

def main():
  fib_list = {}
  fib_list[0] = 1
  fib_list[1] = 1
  n = 1
  while fib_list[n] < 144:
    n += 1
    fib_list[n] = fib_list[n - 2] + fib_list[n - 1] 
  print(n, fib_list)

  n += 1
  results = {}
  while len(results) < 5:
    digit_sum = fib_digit(n, fib_list)
    if fib_list[n] % digit_sum == 0:
      results[n] = fib_list[n]
    n += 1
  print(results)

if __name__ == '__main__':
  main()
