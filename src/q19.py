# Q19 友達の友達は友達？
# １以外の同じ約数を持つ数字を「友達」とします。つまり、２つの数の最大公約数が１でない場合を友達とします。
# １〰Ｎまでの合成数からいずれか１つを選び、この数から他のすべての数にたどり着くには、
# 何段階の友達をたどればよいかを数えます。１〰Ｎまでの「合成数」から７個の数を選んだとき、
# 最大で６段階をたどることになる最小のＮを選んでください。

from itertools import permutations

def isPrime(num, primes):
  for p in primes:
    if num % p == 0:
      return False
  return True

def main():
  primes = []
  num = 2
  length = 6
  while len(primes) < length:
    if isPrime(num, primes):
      primes.append(num)
    num += 1
  
  perms = permutations(range(length), length)
  min_value = float('inf')
  for p in perms:
    nums = [primes[p[0]] ** 2] # a*a
    nums += [primes[p1] * primes[p2] for p1, p2 in zip(p[:-1], p[1:])] # a*b, b*c, c*d, d*e, e*f
    nums.append(primes[p[-1]] ** 2) # f*f
    if min_value > max(nums):
      min_value = max(nums)
      min_nums = nums
  print(min_value, min_nums)

if __name__ == '__main__':
  main()
