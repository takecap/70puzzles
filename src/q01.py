# Q01 10進数で回文
# 問題 10進数、2進数、8進数のいずれで表現しても回文数となる数のうち、
# 10進数の10以上で最小の値を求めてください。

# num_str: str が回文かどうかを判定する
def is_palindrome(num_str):
  return num_str == num_str[::-1]

# num: int が１０進・２進・８進表記で回文かどうかを判定する
def tris_palindrome(num):
  num_dec = str(num)
  num_bin = bin(num)[2:]
  num_oct = oct(num)[2:]
  return is_palindrome(num_dec) and is_palindrome(num_bin) and is_palindrome(num_oct)

def main():
  num = 10
  while True:
    if tris_palindrome(num):
      print(num, bin(num)[2:], oct(num)[2:])
      break
    num += 1

if __name__ == '__main__':
  main()
