# Q42 １つの数字で作る１２３４
# 「１２３４」を１つの数字だけで、できるだけ少ない個数で表現するとき、
# 最も少ない個数で表現できる数字を求め、その式を全て答えてください。

operators = ['', '+', '-', '*', '/']

# digit: 'n', fm: 数式を表す文字列, forms: [fm]
def add(digit, forms):
  results = []
  for fm in forms:
    ret_formulas = [digit + op + fm for op in operators]
    results += ret_formulas
  return results

def main():
  forms = [[str(i)] for i in range(10)]
  step, not_found = 2, True
  while not_found:
    print("Step", step)
    for i in range(1, 10):
      forms[i] = add(str(i), forms[i])
      for fm in forms[i]:
        if int(eval(fm)) == 1234:
          print("GET!", fm, eval(fm))
          not_found = False
    step += 1

if __name__ == '__main__':
  main()
