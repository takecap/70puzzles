# Q66 図形の一筆書き
# 図２０の左側にあるような４つのパターンのパネルがあります。これを縦と横に並べて配置してできる図形を
# 一筆書きすることを考えます。縦に３つ、横に４つ並べたとき、一筆書きできるパターンが何通りあるかを求めてください。
# （ただし、左右の反転、上下の反転などにより同じ形になる場合は別々にカウントするものとします。）

# rows: int, cols: int -> (rows+1) * (cols+1) の長さの bool のリストを返す
# 格子点の状態（頂点の次数が奇数であるかどうか）を表す
def init_status(rows, cols):
  base = [False] + [True] * (cols-1) + [False]
  result = [b for b in base]
  for _ in range(rows-1):
    result += [not b for b in base]
  result += [b for b in base]
  return result

# (i,j) 成分のマスに pattern: 0,1,2,3 を追加したときの status を返す
def put(status, pattern, i, j, cols):
  result = [b for b in status]
  if pattern % 2 == 1:
    result[(cols + 1) * i + j] ^= True
    result[(cols + 1) * (i + 1) + (j + 1)] ^= True
  if pattern // 2 == 1:
    result[(cols + 1) * i + (j + 1)] ^= True
    result[(cols + 1) * (i + 1) + j] ^= True
  return result

# st_list: [status] -> (i,j) 成分のマスに新たな pattern を配置して得られる status のリストを返す
def search(st_list, i, j, cols):
  results = []
  for st in st_list:
    for pt in range(4):
      new_st = put(st, pt, i, j, cols)
      if sum(new_st[:((cols + 1) * i + j + 1)]) < 3:
        # status の (cols+1)*i+j 番までは成分が確定、奇数の点が３つ以上あったら一筆書きは不可能
        results.append(new_st)
  return results

def main():
  rows, cols = 3, 4
  base = init_status(rows, cols)
  print("rows: {:d}, cols: {:d}".format(rows, cols))
  results = [base]
  for i in range(rows):
    for j in range(cols):
      results = search(results, i, j, cols)
  results = [st for st in results if sum(st) < 3]
  print("Total:", len(results))

if __name__ == '__main__':
  main()
