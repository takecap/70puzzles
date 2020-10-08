# Q26 効率のよい立体駐車場
# この立体駐車場では、車が止まっていない位置の交換を繰り返して、出庫位置まで車を移動させます。
# 10 × 10 の駐車場の場合、左上から右下まで最短の手順で移動する手数を求めてください。

def move_blank(blank, target, step):
  return target, step + abs(blank[0] - target[0]) + abs(blank[1] - target[1])

def move(car, blank, step, dir=1):
  if dir:
    target = (car[0], car[1] + 1)
  else:
    target = (car[0] + 1, car[1])
  blank, step = move_blank(blank, target, step)
  return target, car, step + 1

def main(size=10):
  car = (1, 1)
  blank = (size, size)
  step = 0
  print("STEP: {:2d}, AT: {}".format(step, car))
  for _ in range(size - 1):
    car, blank, step = move(car, blank, step, 0)
    car, blank, step = move(car, blank, step, 1)
  print("STEP: {:2d}, AT: {}".format(step, car))

if __name__ == '__main__':
  main(10)
