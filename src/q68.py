# Q68 隣り合わないのがマナー？
# １列の座席で、他人と隣り合わずに座れる場合は他人の隣に座らないことにします。隣り合わないと座れない場合は、
# 空いているところに座っていきます。Ａ〰Ｆ，Ｇ〰Ｌの１２個の座席がある車両に１２人が乗ってくる場合、
# １２人の座る順番が何通りあるかを求めてください。

start = (-1,) + (0,) * 6 + (-1,) + (0,) * 6 + (-1,)

# seats: (int), idx: int, idx 番の席の状態を返す
# 1: 両隣に人がいない空席, 0: 隣に人がいる空席, -1: 使用済席
def state(seats, idx):
  if seats[idx] == 0:
    if seats[idx-1] < 1 and seats[idx+1] < 1:
      return 1
    else:
      return 0
  else:
    return -1

# idx 番の値を 1（使用済）にする
def sit(seats, idx):
  return seats[:idx] + (1,) + seats[idx+1:]

# memo: (seats[1:7], seats[8:14]) を key とし、seats の状態から何通りあるかを value とする辞書
# seats の状態からすべての席に座る順番が何通りあるかを再帰的に探索する
def search(seats, memo):
  key = (seats[1:7], seats[8:14])
  if key in memo:
    return memo[key]
  status = [state(seats, i) for i in range(15)]
  primary = [i for i, s in enumerate(status) if s == 1]
  secondary = [i for i, s in enumerate(status) if s == 0]
  if len(primary) == 0 and len(secondary) == 0:
    return 1
  cnt = 0
  if len(primary) > 0:
    for idx in primary:
      cnt += search(sit(seats, idx), memo)
  else:
    for idx in secondary:
      cnt += search(sit(seats, idx), memo)
  memo[key] = cnt
  return cnt

def main():
  memo = {}
  cnt1 = search(sit(start, 1), memo)
  cnt2 = search(sit(start, 2), memo)
  cnt3 = search(sit(start, 3), memo)
  print("TOTAL:", (cnt1 + cnt2 + cnt3) * 4)

if __name__ == '__main__':
  main()
