# Q03 カードを裏返せ
# 問題 1 〰 100までの番号が書かれた100枚のカードが順番に並べられています。
# n番目のカードからn-1枚おきにカードを裏返す操作を、どのカードの向きも変わらなくなる
# まで続けたとします。そのとき、裏向きになっているカードの番号を全て求めてください。

def main():
  cards = [True] * 101
  for num in range(2, 101):
    for i, c in enumerate(cards):
      if i % num == 0:
        cards[i] = not c
  result = [i for i, c in enumerate(cards) if c and i]
  print(result)

if __name__ == '__main__':
  main()
