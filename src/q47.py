# Q47 オンリーワンな〇×
# n 行 n 列の行列に〇と×を並べ、その行と列について〇の個数をカウントしてみます。
# 逆に、カウントした数字から、行列に〇と×を配置しなおしてみます。すると、同じ数でも異なる配置になることがあります。
# n = 4 のとき、上記のようにカウントした値から配置を変え、１通りにしか配置できないパターンがいくつあるかを答えてください。

# sequence: ['1' or '0'] -> [True or False]
def convert_bool(sequence):
  def cvt(ch):
    return True if ch == '1' else False
  return [cvt(ch) for ch in sequence]

# size: int -> [row]、ただし row: [True or False], len(row) == size
# 長さが size のすべての True or False の列（〇×の列）のリストを返す
def gen_rows(size):
  rows = []
  for i in range(2 ** size):
    num = bin(i)[2:]
    if len(num) < size:
      num = '0' * (size - len(num)) + num
    rows.append(convert_bool(num))
  return rows

# row1 と row2 のなかで、カウントを変えずに入れ替えられる idx が存在するかを判定する
def swappable(row1, row2):
  exors = [idx for idx, (r1, r2) in enumerate(zip(row1, row2)) if r1 ^ r2]
  for i1, i2 in zip(exors[:-1], exors[1:]):
    if row1[i1] ^ row1[i2]:
      return True
  return False

# idxes: [idx0, idx1,...,idxk] お互いに not swappable な row の idx のリスト
# len(idxes) == size のとき、１通りにしか配置できないパターンとなる
def search(idxes, candidates, size, unswappables):
  if len(idxes) == size:
    return 1
  count = 0
  for idx in candidates:
    next_candidates = unswappables[idx] & candidates
    count += search(idxes + [idx], next_candidates, size, unswappables)
  return count

def main():
  num, count = 4, 0
  rows = gen_rows(num)
  # unswappables: r2 in rows に対して、not swappable な r1 in rows の idx のリスト
  unswappables = [ set( idx for idx, r1 in enumerate(rows) if not swappable(r1, r2)) for r2 in rows ]
  for i in range(2 ** num):
    count += search([i], unswappables[i], num, unswappables)
  print("Num: {:d}, TOTAL: {:d} cases".format(num, count))

if __name__ == '__main__':
  main()
