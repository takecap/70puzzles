# Q09 つりあわない男女

# seq: ['B' or 'G']
def unbalance(numB, cntG, maxB, maxG):
  head = numB != cntG # 前から見て、等分割できるかを判定する
  tail = (maxB - numB) != (maxG - cntG) # 後ろから見て、等分割できるかを判定する
  return head and tail

def count(numB, numG, maxB, maxG, memo):
  if (numB, numG) in memo:
    return memo[numB, numG]
  if unbalance(numB, numG, maxB, maxG) and 0 <= numB <= maxB and 0 <= numG <= maxG:
    memo[numB, numG] = count(numB-1, numG, maxB, maxG, memo) + count(numB, numG-1, maxB, maxG, memo)
    return memo[numB, numG]
  else:
    memo[numB, numG] = 0
    return 0

def main():
  maxB, maxG = 20, 10
  memo = {(1,0): 1}
  print("Boy:", maxB)
  print("Girl:", maxG)
  print("Count:", count(maxB-1, maxG, maxB, maxG, memo) + count(maxB, maxG-1, maxB, maxG, memo))

if __name__ == '__main__':
  main()
