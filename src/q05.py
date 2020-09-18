# Q05 いまだに現金払い？
# 問題 10円玉、50円玉、100円玉、500円玉の組み合わせに両替することを考えます。
# 1000円札を入れたときに出てくる硬貨の組み合わせは何通りあるかを求めてください。
# ただし、たくさんの硬貨が出ると困るため、最大で15枚になるように両替するものとします。
#
# TODO: 1000円札以外の両替や、両替に使う金種の変更に対応するよう拡張する
#

def main():
  patterns = []
  coin_pattern = []
  for n500 in range(3):
    for n100 in range(11):
      for n50 in range(15):
        remain = 1000 - 500 * n500 - 100 * n100 - 50 * n50
        n10 = remain // 10
        if n10 >= 0 and n500 + n100 + n50 + n10 <= 15:
          coin_pattern = [n500, n100, n50, n10]
          patterns.append(coin_pattern)
  print(len(patterns))

if __name__ == '__main__':
  main()
