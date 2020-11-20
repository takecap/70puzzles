# Q30 テーブルタップで作るタコ足配線
# ここでは、口数が２つのテーブルタップと３つのテーブルタップがあるものとします。
# 壁のコンセントは１つしか使えない状態で、n 台の電気機器を使いたい場合のテーブルタップの配置を考えます。
# n = 20 の場合、テーブルタップの配置として考えられるのは何通りあるかを求めてください。
# （同じテーブルタップに挿す場合、挿す口の位置は考えないものとし、テーブルタップの結合方法のみを考えます。
# また、口が余ることがないようにテーブルタップを接続します。）

# num: int, memo: num -> cnt の辞書
def search(num, memo):
  if num in memo:
    return memo[num]
  cnt = 0
  for i in range(1, num // 2 + 1):
    if num - i == i:
      # s = search(i, memo) とすると、２口のタップの先にそれぞれ i 台の電気機器を接続するケースを考える
      # s * (s - 1) / 2 (異なる配置) + s (同じ配置) = (s ^ 2 + s) / 2
      cnt += search(i, memo) * (search(i, memo) + 1) // 2
    else:
      cnt += search(num - i, memo) * search(i, memo)
  for i in range(1, num // 3 + 1):
    for j in range(i, (num - i) // 2 + 1):
      if i == j and num - i - j == i:
        # ３口のタップの先にそれぞれ i 台の電気機器を接続するケースを考える
        # s * (s-1) * (s-2) / 6 (３つの異なる配置) + s * (s-1) (２つの異なる配置) + s (３つとも同じ配置) = s * (s+1) * (s+2) / 6
        cnt += search(i, memo) * (search(i, memo) + 1) * (search(i, memo) + 2) // 6
      elif i == j:
        cnt += search(i, memo) * (search(i, memo) + 1) * search(num - i - j, memo) // 2
      elif num - i - j == i:
        cnt += search(i, memo) * (search(i, memo) + 1) * search(j, memo) // 2
      elif num - i - j == j:
        cnt += search(i, memo) * search(j, memo) * (search(j, memo) + 1) // 2
      else:
        cnt += search(num - i - j, memo) * search(i, memo) * search(j, memo)
  memo[num] = cnt
  return cnt

def main():
  num = 20
  memo = {1: 1}
  print("Num:", num)
  print("Total:", search(num, memo))

if __name__ == '__main__':
  main()
