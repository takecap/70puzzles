# Q48 グレイコードのループ
# 数値の符号化法の１つに「グレイコード」があります。ここでは「n進数をグレイコードに変換し、その変換先をn進数と見て、
# さらにグレイコードに変換する」ということを元の値になるまで繰り返してみます。
# n = 16 のとき、「808080」から始めて「808080」に戻るまでの回数と、「abcdef」から始めて「abcdef」に戻るまでの回数
# を答えてください。

baseN = '0123456789abcdef'

# base: int, org: str
# base 進数表記の数字 org をグレイコードに変換して返す
def toGray(base, org):
  gray = ''
  shift = 0
  for ch in org:
    idx = baseN.index(ch)
    val = (idx + shift) % base
    gray = gray + baseN[val]
    shift += base - val
  return gray

# base 進数表記の数字 org から始めて org に戻るまでの回数を求める
def search(base, org):
  temp = toGray(base, org)
  count = 1
  while temp != org:
    temp = toGray(base, temp)
    count += 1
  return count

def main():
  base = 16
  org = '808080'
  print("START:", org)
  count = search(base, org)
  print("STEP: {:d}".format(count))
  org = 'abcdef'
  print("START:", org)
  count = search(base, org)
  print("STEP: {:d}".format(count))

if __name__ == '__main__':
  main()
