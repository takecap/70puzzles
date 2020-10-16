# Q36 「０」と「７」の回文数

# 0 or 7 で構成される数字のジェネレータ
def gen_70num():
  num = 1
  while True:
    yield int(bin(num)[2:]) * 7
    num += 1

# num: int, candidates: set(int)
# candidates のうち、num の因数である数字の集合を返す
def search_factors(num, candidates):
  results = set()
  for i in candidates:
    if num % i == 0:
      results.add(i)
  return results

def main():
  count = 0
  candidates = set(range(1, 51))
  candidates.remove(13)
  results = {} # key: gen_70num で生成された数字, value: key の因数の集合
  for num in gen_70num():
    factors = search_factors(num, candidates)
    results[num] = factors
    candidates -= factors
    count += 1
    if candidates == set() or count > 10000:
      break
  count = 0
  for key in results.keys():
    if str(key) == str(key)[::-1]:
      factors = results[key]
      for num in factors:
        print("{:2d} * {:d} = {:d}".format(num, key // num, key))
        count += 1
  print("TOTAL:", count, "cases")

if __name__ == '__main__':
  main()
