# Q65 面倒なキャッチボール
# １から１２の番号を付け、キャッチボールを繰り返して１番の学生が持っているボールを１２番の学生に渡すことを考えます。
# ただし、次のような条件があります。
# 1. １人が持つことができるボールは１つだけ
# 2. 同時に投げられるのは１人だけで、必ず受ける相手がいる
# 3. 最初は１〰１１番の学生がボールを持っている
# 4. どの学生も投げられるのは向かい合う３カ所だけ
# 5. キャッチボールが終わったとき、１番の学生と１２番の学生以外は最初のボールを持っている
# 最小の回数で１番の学生が持っているボールを１２番の学生に渡し、条件５を満たすとき、ボールを投げる回数の合計を
# 求めてください。なお、それぞれのボールは識別できるものとします。

# catch: int, ボールを持っていない人の idx
def target(catch):
  line, idx = 1 - catch // 6, catch % 6
  if idx == 0:
    return [(line * 6 + i) for i in range(2)]
  elif idx == 5:
    return [(line * 6 + i + 4) for i in range(2)]
  else:
    return [(line * 6 + idx + i - 1) for i in range(3)]

# balls: (int), 持っているボールの番号のタプル
# ボールを持っていない人が pitch からボールを受け取った後の状態をタプルで返す
def exchange(balls, pitch):
  catch = balls.index(-1)
  result = list(balls)
  result[catch] = result[pitch]
  result[pitch] = -1
  return tuple(result)

# balls_status: [balls], balls から遷移できる状態の集合を返す
def step(balls_status):
  status = set()
  for balls in balls_status:
    catch = balls.index(-1)
    for idx in target(catch):
      status.add(exchange(balls, idx))
  return status

def main():
  start = tuple(i for i in range(11)) + (-1,)
  goal = (-1,) + tuple(i for i in range(1, 11)) + (0,)
  fwds, bcks = set(), set()
  dfwds, dbcks = {start}, {goal}
  times = 1
  while times < 100:
    temp = step(dfwds)
    if temp & dbcks:
      print("Got", times)
      break
    fwds |= dfwds
    dfwds = temp - fwds
    times += 1
    temp = step(dbcks)
    if temp & dfwds:
      print("Got", times)
      break
    bcks |= dbcks
    dbcks = temp - bcks
    times += 1

if __name__ == '__main__':
  main()
