# Q07 日付の２進数変換
# 年月日をYYYYMMDDの８桁の整数で表したとき、これを２進数に変換して逆に並べ、
# さらに１０進数に戻したとき、元の日付と同じ日付になるものを探してください。
# 探索する期間は19641010 〰 20200724とします。

from datetime import date
from datetime import timedelta

# dt: datetime.date を２進数に変換して返す
def date2bin(dt):
  date_str = dt.strftime('%Y%m%d')
  return bin(int(date_str))[2:]

def main():
  dt = date(1964, 10, 10)
  while dt < date(2020, 7, 25):
    date_bin = date2bin(dt)
    if date_bin == date_bin[::-1]:
      print(dt, date_bin)
    dt += timedelta(days=1)

if __name__ == '__main__':
  main()
