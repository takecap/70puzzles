# Q16 ３本のひもで作る四角形
# 同じ長さの３本のひもを折り曲げて３つの四角形を作ることを考えます。
# そのうち２本でそれぞれ長方形を作り、残りの１本は正方形を作ります。
# ひもの長さを１から５００まで変化させるとき、２つの長方形の面積の和と、
# 正方形の面積が同じになる組が何通りあるかを求めてください。
# ただし、いずれの長方形・正方形も辺の長さは整数になるものとします。

squared = [i * i for i in range(125)]

# １辺が n の正方形に対して、２つの長方形の和が等しくなるような組を探索する
def search_balance(n):
  results = []
  for a in range(1, n //2 + 1):
    # n ^ 2 = a * (2n - a) + b * (2n - b) を b について解くと
    # b = n - sqrt(n ^ 2 - (n - a) ^ 2) なので、sqrt の中身が平方数なことが必要条件
    val = n * n - (n - a) * (n - a)
    if val in squared:
      b = n - round(val ** 0.5)
      if (n, b, a) in results:
        continue
      results.append((n, a, b))
  return results

def main():
  patterns = []
  for n in range(126):
    patterns += search_balance(n)
  keys = set()
  results = []
  for pattern in patterns:
    rate = pattern[0] / pattern[1]
    if not rate in keys:
      keys.add(rate)
      results.append(pattern)
  print('RESULT:', len(keys))
  for res in results:
    print(res)

if __name__ == '__main__':
  main()
