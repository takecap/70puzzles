# Q22 絡まない糸電話
# 同一円周上に等間隔に並んだ子どもたちが、ペアを組んで糸電話で会話しようとしています。
# このとき、交差してしまうと、糸が絡まってしまいますので、交差しないような相手とペアを組む必要があります。
# １６人の子どもたちがいた場合、作ることができるペアが何通りあるかを求めてください。

# sequence: [int] まだペアが定まっていない子供たちの番号のリスト
def search(sequence):
  size = len(sequence)
  if size == 2:
    return [[tuple(sequence)]]
  else:
    results = []
    last_idx = size - 1
    for i in range(size // 2):
      idx = 2 * i + 1
      if idx == 1: # 先頭の２人でペアを組み、残りの子供たちの結果と合わせる
        pair = tuple(sequence[:2])
        seq = search(sequence[2:])
        results += [[pair] + s for s in seq]
      elif idx == last_idx: # 先頭と最後尾の２人でペアを組み、残りの子供たちの結果と合わせる
        seq = search(sequence[1:-1])
        pair = (sequence[0], sequence[-1])
        results += [s + [pair] for s in seq]
      else: # 先頭と idx 番目の２人でペアを組み、1...idx-1 と idx+1...last_idx の各グループの結果と合わせる
        pair = (sequence[0], sequence[idx])
        seq1 = search(sequence[1:idx])
        seq2 = search(sequence[idx+1:])
        for s1 in seq1:
          results += [[pair] + s1 + s2 for s2 in seq2]
    return results

def main():
  results = search(list(range(16)))
  print("RESULTS: ", len(results))

if __name__ == '__main__':
  main()
