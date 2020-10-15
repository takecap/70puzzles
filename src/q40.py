# Q40 並べ替えの繰り返し
# 1,2,3,...,n というラベルが付いた n 枚のカードがあります。
# １枚目のカードのラベルが k のとき、最初の k 枚のカードを逆順にする、という操作を繰り返すことを考えます。
# n = 9 のとき、カードが変化しなくなるまでの回数が最も多くなるような９枚の並びを求めてください。

from itertools import permutations

# cards: 1..num の permutation の tuple でカードの並びを表現する
# cards を key とし、変化しなくなるまでの回数を value とする dict を返す
# value の初期値は -1 とする
def init_steps(num):
  return {cards: -1 for cards in permutations(range(1, num+1), num)}

# cards を初期配置とし、変化しなくなったときのカードの並びと操作回数を返す
def move(cards):
  num = 0
  while cards[0] != 1:
    idx = cards[0]
    cards = flip(cards, idx)
    num += 1
  return cards, num

# cards の 0..idx を逆順にする操作を行ったカードの並びを返す
def flip(cards, idx):
  return cards[idx-1::-1] + cards[idx:]

# １回の操作で cards に変化するカードの並びのリストを返す
def back_candidates(cards):
  indexes = [num for idx, num in enumerate(cards[1:], 2) if idx == num]
  return [flip(cards, idx) for idx in indexes]

# cards_list: [cards] について、１回の操作で [cards] のいずれかに変化するカードの並びのリスト next_list を探索する
# 見つかったカードの並びについて steps_dict を更新し、next_list について再帰的に back を行う
# next_list == [] の時に探索を終了し、その時点の step を返す
def back(cards_list, step, steps_dict):
  next_list = []
  for cards in cards_list:
    next_list += back_candidates(cards)
  if next_list == []:
    return step
  for cards in next_list:
    steps_dict[cards] = step+1
  return back(next_list, step+1, steps_dict)

def main():
  num = 9
  steps_dict = init_steps(num)
  max_steps = 0
  for cards in steps_dict.keys():
    if steps_dict[cards] > -1 or cards[0] != 1:
      continue
    steps_dict[cards] = 0
    cards_list = [cards]
    step = back(cards_list, 0, steps_dict)
    if step > max_steps:
      max_steps = step
  
  undone = [cards for cards in steps_dict.keys() if steps_dict[cards] < 0]
  if len(undone) > 0:
    print("UNDONE:", len(undone), "cases")
    for cards in undone[:10]:
      print(cards)
    return
  print("MAX STEP:", max_steps)
  max_step_cards = [cards for cards in steps_dict.keys() if steps_dict[cards] == max_steps]
  for cards in max_step_cards:
    goal, num = move(cards)
    print(cards, "->", goal)

if __name__ == '__main__':
  main()
