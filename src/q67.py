# Q67 クロスワードパズルを作成せよ
# クロスワードパズルは縦と横に交差したマスに言葉を当てはめていくパズルです。文字の入るマス（白マス）と
# 入らないマス（黒マス）があり、その配置には以下のような条件があります。
# ・黒マスは縦横に連続しない
# ・黒マスによって盤面が分断されてはいけない
# 横に６マス、縦に５マスのクロスワードパズルを考えるとき、上記の２つの条件を満たすような配置が
# いくつあるかを求めてください。（黒と白の配置のみを考え、そこに入る文字については考えないものとします。）

# rows: int, cols: int -> (rows+2) * (cols+2) のサイズのリストのリストの集合を返す
# 白マスを 0, 黒マスを 1, 壁を -1 で表現し、黒マスが連続する盤面は results に入らないようにする
def candidates(rows, cols):
  start = [[-1 for _ in range(cols+2)] for _ in range(rows+2)]
  results = [start]
  for i in range(1, rows+1):
    for j in range(1, cols+1):
      diff = []
      for arrange in results:
        if arrange[i-1][j] == 1 or arrange[i][j-1] == 1:
          arrange[i][j] = 0
        else:
          temp = [[val for val in row] for row in arrange]
          arrange[i][j] = 1
          temp[i][j] = 0
          diff.append(temp)
      results += diff
  return results

# arrange: [[int]] -> 盤面の白マスが連結しているかどうかを判定する
def check(arrange):
  all = sum(arrange, []).count(0)
  start = arrange[1].index(0)
  found, diff = set(), {(start, 1)}
  while len(diff) > 0:
    temp = set()
    for (x, y) in diff:
      if arrange[y][x-1] == 0:
        temp.add((x-1, y))
      if arrange[y][x+1] == 0:
        temp.add((x+1, y))
      if arrange[y-1][x] == 0:
        temp.add((x, y-1))
      if arrange[y+1][x] == 0:
        temp.add((x, y+1))
    found |= diff
    diff = temp - found
  return all == len(found)

def main():
  rows, cols = 5, 6
  print("Row: {:d}, Col: {:d}".format(rows, cols))
  arranges = candidates(rows, cols)
  print("Candidates:", len(arranges))
  results = [arr for arr in arranges if check(arr)]
  print("Total:", len(results))

if __name__ == '__main__':
  main()
