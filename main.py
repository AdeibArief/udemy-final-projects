import pycountry
text="i love my country india"
for country in pycountry.countries:
    if country.name in text:
        print(country.name)
