# Q45 素数のマトリックス

# num: int が素数か判定する
def isPrime(num):
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True

# start...end の範囲の素数を出力するジェネレータ
def gen_primes(start, end):
  num = start
  while not isPrime(num):
    num += 1
  while num < end:
    yield num
    num += 2
    while not isPrime(num):
      num += 2

# ３桁の素数のリスト
primes = [str(n) for n in gen_primes(100, 1000)]

# pr0: [p0, p1, p2] ３つの素数からなるリスト
# pr0 を０行目とする素数のマトリックスを探索する
def search(pr0):
  candidates = set(primes) - {pr0}
  results = set()

  col0s = { pc for pc in candidates if pc[0] == pr0[0] } # pr0[0] と 100 の桁の数が一致する素数が候補となる
  for pc0 in col0s: # pr0 を０行目、pc0 を０列目とする素数のマトリックスを探索する
    row1s = { pr for pr in candidates - {pc0} if pr[0] == pc0[1] } # pc0[1] と 100 の桁の数が一致する素数が候補となる
    for pr1 in row1s: # pr0 を０行目、pr1 を１行目、pc0 を０列目とする素数のマトリックスを探索する
      # pr0[1] と 100 の桁、 pr1[1] と 10 の桁の数が一致する素数が候補となる
      col1s = { pc for pc in candidates - {pc0, pr1} if pc[0] == pr0[1] and pc[1] == pr1[1]}
      for pc1 in col1s: # pr0 を０行目、pr1 を１行目、pc0 を０列目、pc1 を１列目とする素数のマトリックスを探索する
        # pr0[2] と 100 の桁、pr1[2] と 10 の桁の数が一致する素数が候補となる
        row2s = { pr for pr in candidates - {pc0, pr1, pc1} if pr[0] == pc0[2] and pr[1] == pc1[2] }
        for pr2 in row2s:
          pc2 = pr0[2] + pr1[2] + pr2[2]
          if pc2 in candidates - {pc0, pr1, pc1, pr2}:
            results.add((pr0, pr1, pr2, pc0, pc1, pc2))
  return results

def main():
  results = set()
  for pr0 in primes:
    results |= search(pr0)
  print("TOTAL: {:d} cases".format(len(results)))

if __name__ == '__main__':
  main()
