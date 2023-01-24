# ZADANIE 1
print("ZADANIE 1\n")
shopping_list = {
  "piekarnia" : ["chleb", "bułki", "pączek"],
  "warzywniak" : ["marchew", "seler", "rukola"]
}

print("Lista zakupów")

for shop in shopping_list:
  for shops in range(len(shopping_list[shop])):
    shopping_list[shop][shops] = shopping_list[shop][shops].capitalize()

  print(f"Idę do {shop}, kupuję tu następujące rzeczy: {shopping_list[shop]}")


suma = len(shopping_list[shop][shops])
print(f"W sumie kupuję {suma} produktów.")

print("Nowy wpis")
print("Kolejny nowy wpis")
print("To teraz jest wysłana wiadomość z repozytorium zdalnego na lokalne")
print("tak to sie mozemy bawić w nieskończoność!!!!")
print("jest fajnie zdalnie ale tez fajnie lokalnie")
