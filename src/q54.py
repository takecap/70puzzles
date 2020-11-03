# Q54 同じ数字で挟み撃ち
# 1 から n までの数字が書かれたカードが２枚ずつ、全部で 2n 枚あります。これを１列に並べ、２枚の「１」の間には
# カードが１枚、２枚の「２」の間にはカードが２枚、…、というように２枚の「n」の間にはカードが n 枚挟まれているように
# 並べることを考えます。n = 11 のとき、何通りの並べ方があるかを求めてください。

# sequence: [int], num: int, idx: int
# sequence は配置された数字を記録するリスト、未配置の位置には -1 が置かれている
# 与えられた数字 num を idx 番目に配置できるかどうかを判定する
def arrangable(sequence, num, idx):
  if idx + num + 1 > len(sequence) - 1:
    return False
  if sequence[idx] > 0 or sequence[idx+num+1] > 0:
    return False
  return True

# sequence に num を再帰的に追加し、可能な並べ方の総数を探索する
def search(sequence, num):
  if num == 0:
    return [sequence]
  results = []
  for idx, _ in enumerate(sequence):
    if arrangable(sequence, num, idx):
      new_sequence = [i for i in sequence]
      new_sequence[idx] = num
      new_sequence[idx+num+1] = num
      results += search(new_sequence, num-1)
  return results

def main():
  num = 11
  sequence = [-1] * (num * 2)
  print("Size:", num)
  results = search(sequence, num)
  print("Results:", len(results))

if __name__ == '__main__':
  main()
