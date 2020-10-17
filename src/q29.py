# 合成抵抗で作る黄金比
# 抵抗値が１Ωの抵抗が n 個あります。これを組み合わせて、抵抗値を「黄金比」である 1.6180339887... に近づけたいと思います。
# n = 10 のとき、組み合わせてできる抵抗値のうち、黄金比に最も近い値を小数第１０位まで求めてください。

target_ratio = 1.6180339887

# values: { float }、抵抗値の集合
# もう１つ抵抗を追加することで実現できる抵抗値の集合を返す
def add_resistance(values):
  results = set()
  for res in values:
    results.add(res + 1)
    results.add(1 / (1 / res + 1))
  return results

def main():
  values = { 1 }
  print("Num:{:2d}, Best:{:.10f}".format(1, target_ratio - 1))
  for i in range(9):
    values = add_resistance(values)
    best_res, best_value = 0, target_ratio
    for res in values:
      if abs(res - target_ratio) < best_value:
        best_res, best_value = res, abs(res - target_ratio)
    print("Num:{:2d}, Best:{:.10f}".format(i+2, best_res))

if __name__ == '__main__':
  main()
