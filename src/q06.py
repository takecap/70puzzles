# Q06 （改造版）コラッツの予想
# ・n が偶数の場合は n を２で割り、奇数の場合は n に３をかけて１を足す
# という操作を繰り返すと、必ず１に到達する（コラッツの予想）
# 今回は、初期値が偶数の場合に「初回のみ n に３をかけて１を足す」ようにする
# このとき、「最初の数」に戻るものを考えます。
# 10000以下の偶数のうち、「最初の数に戻る数」がいくつあるか、個数を求めてください。

def next(n):
  if n % 2 == 0:
    return n // 2
  else:
    return n * 3 + 1

# n: int 改造版コラッツの予想に基づく操作を繰り返したとき、「最初の数に戻る」かどうかを判定する
def collatz(n):
  if n % 2 != 0:
    return False
  val = n * 3 + 1
  while True:
    val = next(val)
    if val == 1:
      return False
    elif val == n:
      return True

def main():
  results = []
  for n in range(2, 10001, 2):
    if collatz(n):
      results.append(n)
  print(len(results), results)

if __name__ == '__main__':
  main()
