# Q51 パーフェクトシャッフル
# 2n 枚のカードを積み重ねて、真ん中で n 枚ずつに分けたあと、それぞれの上から順に１枚ずつ取り出して
# 重ねていく、という作業を「シャッフル」と呼ぶことにします。シャッフルを何回か繰り返すと、元の順番と同じになります。
# 2(n-1) 回で元に戻るような n が 1 < n < 100 までの間にいくつあるかを求めてください。

def shuffle(sequence):
  n = len(sequence) // 2
  seq0 = sequence[:n]
  seq1 = sequence[n:]
  result = ()
  for n0, n1 in zip(seq0, seq1):
    result += (n0, n1)
  return result

# n: int, 元に戻るまでに何回のシャッフルが必要かを返す
def count(n):
  goal = tuple(i for i in range(2 * n))
  seq = tuple(i for i in range(2 * n))
  step = 0
  while True:
    seq = shuffle(seq)
    step += 1
    if seq == goal or step > 2 * n - 2:
      return step

# 2(n-1) 回のシャッフルを繰り返したとき、元に戻るかを判定する
def check(n):
  goal = tuple(i for i in range(2 * n))
  seq = tuple(i for i in range(2 * n))
  times = 2 * n - 2
  for _ in range(times):
    seq = shuffle(seq)
  return seq == goal

def main():
  cnt = 0
  for i in range(1, 101):
    if check(i):
      cnt += 1
  print("2(n-1) 回で元に戻る: ", cnt)
  cnt = 0
  for i in range(1, 101):
    if count(i) == 2 * i - 2:
      cnt += 1
  print("2(n-1) 回で初めて元に戻る: ", cnt)

if __name__ == '__main__':
  main()
