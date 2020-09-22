# Q14 Ｗ杯出場国しりとり
# どの国名も一度しか使うことができないとき、最も長く続けられる順を求め、
# 使用した国名の数を答えてください。

countries = [
  'Brazil', 'Croatia', 'Mexico', 'Cameroon', 'Spain', 'Netherlands',
  'Chile', 'Australia', 'Columbia', 'Greece', "Cote d'Ivoire", 'Japan',
  'Uruguay', 'Costa Rica', 'England', 'Italy', 'Switzerland', 'Ecuador',
  'France', 'Honduras', 'Argentina', 'Bosnia and Herzegovina', 'Iran', 'Nigeria',
  'Germany', 'Portugal', 'Ghana', 'USA', 'Belgium', 'Algeria', 'Russia', 'Korea Republic'
]

# country_sequence: [country_name] 考慮中のしりとり（国名の列）
# candidates: [country_name] まだ使用されていない国名のリスト
# results: [country_sequence] 完成した（行き詰まりになった）しりとりのリスト
# country_sequence に続く国名の列を candidates に残った国名から再帰的に探索する
# しりとりの列が完成したら（それ以上続けられなくなったら）country_sequence を resultsに追加する
def search_sequence(country_sequence, candidates, results):
  country = country_sequence[-1]
  next_countries = [candidates[idx] for idx, name in enumerate(candidates) if name[0] == country[-1]]
  if next_countries == []:
    results.append(country_sequence)
  for country in next_countries:
    seq = country_sequence + [country]
    cands = [name for name in candidates if name != country]
    search_sequence(seq, cands, results)

# country: str で始まる全てのしりとりの列を探索する
# 探索結果の中で最長のしりとりの列を返す
def search(country):
  candidates = [name.upper() for name in countries if name != country]
  results = []
  search_sequence([country.upper()], candidates, results)
  longest = sorted(results, key=lambda seq: len(seq), reverse=True)[0]
  return longest

def main():
  longest_sequences = [search(country) for country in countries]
  sorted_sequences = sorted(longest_sequences, key=lambda seq: len(seq), reverse=True)
  for i in range(3):
    print(len(sorted_sequences[i]), sorted_sequences[i])

if __name__ == '__main__':
  main()
