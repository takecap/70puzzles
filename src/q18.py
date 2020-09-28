# Q18 ショートケーキの日
# ホールケーキを切り分けるとき、ケーキに乗っているイチゴの数がすべて異なるような切り方を考えてみましょう。
# Ｎ個に切り分けるときには「１〰Ｎ個のイチゴ」がそれぞれに乗っているようにします。
# ただし、「隣り合う２つのケーキに乗っているイチゴの数の和が、いずれも平方数になるように切らなければならない」
# という条件を追加します。条件を満たすような切り方ができる最小のＮを求めてください。

# n: int, sequence: [int], square_list: [1, 4, ..., n^2]
def check(n, sequence, square_list):
  # １〰Ｎまで全て使い切ったとき、最後尾と先頭の和が平方数になれば条件が成立
  if len(sequence) == n:
    if sequence[0] + sequence[-1] in square_list:
      print(sequence)
      return True
  else:
    tail = sequence[-1]
    for num in range(1, n + 1):
      # 「まだ使用されていない」かつ「現在の末尾との和が平方数になる」数を sequence に追加する
      if (not num in sequence) and tail + num in square_list:
        if check(n, sequence + [num], square_list):
          return True
      else:
        continue
    return False

def main():
  num = 1
  squares = [1]
  while True:
    num += 1
    squares.append(num * num)
    if check(num, [1], squares):
      print(num, "GOT!")
      break

if __name__ == '__main__':
  main()
