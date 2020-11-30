# Q63 カレンダーの最大長方形
# １ヵ月ごとのカレンダーにおいて、それぞれの月で内側に「平日だけ」が入る最大の長方形を調べます。
# 平日は土曜・日曜・祝日以外とし、月をまたぐことはできないものとします。
# 2006 年〰 2015 年の１０年間で、各月の「平日だけ」が入る最大の長方形を求め、１２ヵ月分の面積の和を答えてください。

from datetime import date, timedelta

holidays = {}
for y in range(2006, 2016):
  for m in range(1, 13):
    holidays['{:d}/{:02d}'.format(y, m)] = []
with open('data/q63.txt', encoding='utf-8') as f:
  for row in f.readlines():
    holidays[row[:7]].append(int(row[8:10]))

# year, month -> その月の日数（末日の日付）を date 型で返す
def endofmonth(year, month):
  if month == 12:
    return date(year+1, 1, 1) - timedelta(days=1)
  else:
    return date(year, month+1, 1) - timedelta(days=1)

# 平日を True, それ以外を False で表した週ごとのリストを返す
def boolcal(year, month):
  df, dl = date(year, month, 1), endofmonth(year, month)
  result = [[ i < 5 and i >= df.weekday() for i in range(7) ]]
  remain = dl.day - (7 - df.weekday())
  for _ in range(remain // 7):
    result.append([ i < 5 for i in range(7) ])
  if remain % 7 > 0:
    result.append( [ i < 5 and i <= dl.weekday() for i in range(7) ])
  for h in holidays["{:d}/{:02d}".format(year, month)]:
    num = h + df.weekday() - 1
    i, j = num // 7, num % 7
    result[i][j] = False
  return result

def count(bc):
  score = 0
  counts = [0] * len(bc)
  counts[0] = [1 if b else 0 for b in bc[0][:6]]
  for i in range(1, len(bc)):
    counts[i] = [counts[i-1][j] + 1 if b else 0 for j, b in enumerate(bc[i][:6])]
    temp = search(counts[i])
    if score < temp:
      score = temp
  return score

def search(week):
  nums = list(set(week[:-1]))
  nums.sort()
  res = nums[0] * 5
  for num in nums[1:]:
    temp = -1
    for c in week:
      if c >= num:
        temp += num
      else:
        if temp > res:
          res = temp
        temp = 0
  return res

def disp(bc):
  for w in bc:
    print(['0' if b else 'X' for b in w])

def main():
  cnt = 0
  for y in range(2006, 2016):
    for m in range(1, 13):
      bc = boolcal(y, m)
      cnt += count(bc)
    print("Year {:d}, Count: {:d}".format(y, cnt))

if __name__ == '__main__':
  main()
