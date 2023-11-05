countries = input().split(', ')
capitals = input().split(', ')
# zipped = {countries[i]: capitals[i] for i in range(len(countries))}
zipped = dict(zip(countries, capitals))
for country, capital in zipped.items():
    print(f"{country} -> {capital}")