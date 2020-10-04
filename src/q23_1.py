# Q23 ブラックジャックで大儲け？

def search(coin, times, results):
  if (coin, times) in results:
    return results[(coin, times)]
  if times == 0:
    results[(coin, times)] = 1
    return 1
  else:
    val = search(coin+1, times-1, results)
    if coin > 1:
      val += search(coin-1, times-1, results)
    results[(coin, times)] = val
    return val

def main():
  results = {}
  print('SEARCHING...')
  print('TOTAL: ', search(10, 24, results))

if __name__ == '__main__':
  main()
