# Q41 美しい？ＩＰアドレス
# １０進数で０〰９の１０個の数字を「一度ずつ」使って表現されるＩＰアドレスを考えます。
# 上記のようなＩＰアドレスを２進数で表現したとき、「左右対称」になるものがいくつあるかを調べ、
# その個数を答えてください。（２進数で表現するときは先頭の０は除かないものとし、３２文字で表現するとします。

# num: 0..255 と２進数で表現したときに num と左右対称になる数字のペア（tuple）のリスト
pairs = [(str(num), str(int(format(num, '08b')[::-1], 2))) for num in range(256)]

# pair: (str, str), num: int
# pair に含まれる２つの値に使われる数字が０〰９の num 個の数字を「一度ずつ」使っているかどうかを判定する
def digits(pair, num):
  if len(pair[0] + pair[1]) != num:
    return False
  flags = [False] * 10
  for d in pair[0] + pair[1]:
    flags[int(d)] = True
  return sum(flags) == num

def search_pairs(n0=5):
  n1 = 10 - n0
  results = []
  candidates0 = [pair for pair in pairs if digits(pair, n0)] # n0 個の数字を使う pair のリスト
  candidates1 = [pair for pair in pairs if digits(pair, n1)] # 10-n0 個の数字を使う pair のリスト
  for p0 in candidates0:
    for p1 in candidates1:
      flags = [False] * 10
      for d in p0[0] + p0[1] + p1[0] + p1[1]:
        flags[int(d)] = True
      if sum(flags) == 10: # p0, p1 で１０個の数字を使う組合せを探す
        results.append((p0, p1))
  return results

def main():
  pairs = []
  for n0 in range(4, 7):
    pairs += search_pairs(n0)
  for (p00, p01), (p10, p11) in pairs:
    print(p00 + '.' + p10 + '.' + p11 + '.' + p01)
  print("TOTAL:", len(pairs), "cases")

if __name__ == '__main__':
  main()
