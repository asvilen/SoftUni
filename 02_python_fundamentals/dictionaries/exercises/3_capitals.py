countries = input().split(", ")
capitals = input().split(", ")
country_capital = {country: capital for (country, capital) in zip(countries, capitals)}

for country in country_capital:
    print(f"{country} -> {country_capital[country]}")