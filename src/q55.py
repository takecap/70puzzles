# Q55 横着なそろばん
# 今回はそろばんを使った足し算をしてみましょう。求めるものは「１から１０までの和」です。
# この計算をするときの、玉を移動する量に着目します。「１から１０までの和」を求めるときに、
# そろばんの玉を移動する量が最小になるような足し算の順番を求め、その計算の最中に移動する
# 玉の数がいくつあるかを答えてください。

from itertools import permutations

# status: [上がっている１の玉の数、５の玉の数、１０の玉の数、５０の玉の数] -> value: 表現されている数字
def st2val(status):
  return status[0] + status[1] * 5 + status[2] * 10 + status[3] * 50

# value -> status
def val2st(value):
  digit1, digit2 = value % 10, value // 10
  return (digit1 % 5, digit1 // 5, digit2 % 5, digit2 // 5)

# num: 新しく足す数, next_status: status に num を追加した結果の状態, count: num を追加する際の玉の移動量
def add(status, num):
  val = st2val(status) + num
  next_status = val2st(val)
  count = sum(abs(i - j) for i, j in zip(status, next_status))
  return next_status, count

# sequence: 「１から１０までの数字の並び」, results: { (status, num): next_status, cnt }
# cnt: sequence の順に数字を足したときの玉の移動の総量
def count(sequence, results):
  status, cnt = (0,0,0,0), 0
  for num in sequence:
    if (status, num) in results:
      status, diff = results[status, num]
    else:
      status, diff = add(status, num)
    cnt += diff
  return cnt

def main():
  results, minCount = {}, 100
  for seq in permutations(range(10, 0, -1), 10):
    temp = count(seq, results)
    if temp < minCount:
      print(temp, seq)
      minCount = temp
  print("Min:", minCount)

if __name__ == '__main__':
  main()

def count2(sequence, status, results):
  if sequence in results:
    return results[sequence]
  status, cnt = add2(status, sequence[0])
  results[sequence[1:]] = count2(sequence[1:], status, results)
  return results[sequence[1:]] + cnt

def add2(status, num):
  val = st2val(status) + num
  next_status = val2st(val)
  count = sum(abs(i - j) for i, j in zip(status, next_status))
  return next_status, count

def main2():
  results, minCount = {(): 0}, 100
  for seq in permutations(range(10, 0, -1), 10):
    temp = count2(seq, (0,0,0,0), results)
    if temp < minCount:
      print(temp, seq)
      minCount = temp
  print("Min:", minCount)
