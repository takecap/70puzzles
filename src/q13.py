# Q13 覆面算を満たすのは何通り？
# 以下の式を満たすような数字のあてはめ方は何通りあるか求めてください。
# READ + WRITE + TALK = SKILL

import re
from itertools import permutations
from copy import copy
nums = [str(i) for i in range(10)] # ['0', '1', ... , '9']
equation = 'READ+WRITE+TALK==SKILL'

# r: int numsから r個を取り出す全ての順列 (n_1, n_2, ... , n_r) のリストを返す
def digit_permutations(r):
  if 1 <= r <= 10:
    return list(permutations(nums, r))
  else:
    return []

# eq_str: str で使われている文字の集合を返す
def get_chars(eq_str):
  m = re.split(r'\W+', eq_str)
  words = ''.join(m)
  return set(words)

# eq_str: str の数字の最上位桁に使われている文字のリストを返す
def get_heads(eq_str):
  m = re.split(r'\W+', eq_str)
  return [w[0] for w in m]

# exp_str: str が評価できるかを判定する
def eval_exp(exp_str):
  m = re.search(r'[a-zA-Z]', exp_str)
  if m:
    return False
  return eval(exp_str)

def main():
  char_set = get_chars(equation)
  heads = get_heads(equation)
  perm10 = digit_permutations(len(char_set))
  results = []
  for perm in perm10:
    expression = copy(equation)
    for j, ch in enumerate(char_set):
      if perm[j] == '0' and ch in heads:
        break
      expression = expression.replace(ch, perm[j])
    if eval_exp(expression):
      results.append(expression.replace('==', '='))
  for exp in results:
    print(exp)
  print('計 {:d} 通り'.format(len(results)))

if __name__ == '__main__':
  main()
