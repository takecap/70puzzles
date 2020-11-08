# Q53 いたずらされたお菓子

def update(remain, idx, diff):
  result = [num for num in remain]
  result[idx] += diff
  return tuple(result)

# candy: お菓子の種類の数, remain: 長さが candy のタプル、残った包み紙の数を保持する
# color: 0..(candy * num - 1) 対象となるお菓子のインデックス, memo: (remain, color) を key として包み方の数を value とする dict
def search(remain, candy, color, memo):
  if remain == (0, ) * candy:
    return 1
  if (remain, color) in memo:
    return memo[(remain, color)]
  cnt = 0
  for idx, rem in enumerate(remain):
    if idx != color % len(remain) and rem > 0: # お菓子(color)を包み紙(idx)で包む場合の包み方を数える
      remain = update(remain, idx, -1)
      cnt += search(remain, candy, color+1, memo)
      remain = update(remain, idx, +1)
  memo[(remain, color)] = cnt
  return cnt

def main():
  candy, num = 5, 6
  remain = (num, ) * candy
  memo = {}
  print("Candy:", candy, "Num:", num)
  print("TOTAL:", search(remain, candy, 0, memo))

if __name__ =='__main__':
  main()
