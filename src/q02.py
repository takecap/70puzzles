# Q02 数列の四則演算
# 問題 並んでいる数字の各桁の間に四則演算の演算子を入れて計算することにします。
# 1000 〰 9999のうち、計算した結果が「元の数の桁を逆から並べた数字」と
# 同じになるものを求めてください。
#
# TODO: eval() を使わずに formula を評価するように修正
# 逆ポーランド記法に変換し、スタックマシンとして評価する
#

import re
operators = ['', '+', '-', '*', '/']

# num: int が問題の条件を満たすかどうかを判定する
# 1000 <= num <= 9999 を対象とする
def has_reverse(num):
  num_str = str(num)
  if len(num_str) != 4:
    return False
  for op1 in operators:
    for op2 in operators:
      for op3 in operators:
        formula = num_str[0] + op1 + num_str[1] + op2 + num_str[2] + op3 + num_str[3]
        match = re.search(r'0+\d+', formula)
        if match:
          m_str = match.group(0)
          formula = formula.replace(m_str, str(int(m_str)))
        if judge_reverse(num_str, formula):
          print("{}: {}={}".format(num_str, formula, eval(formula)))
          return True
  return False

# num_str: str, formula: str
# オリジナルの数字と formula の四則演算結果が逆順になっているかを判定する
def judge_reverse(num_str, formula):
  if len(formula) == 4:
    return False
  try:
    result = eval(formula)
  except ZeroDivisionError:
    return False
  res_str = str(round(result))
  return num_str == res_str[::-1]

def main():
  for num in range(1000, 10000):
    if has_reverse(num):
      break

if __name__ == '__main__':
  main()
