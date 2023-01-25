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
print("teraz to bede sobie caly czas przesyłał informacje z jednego repo do drugiego")
print("teraz juz chyba rozumiem działanie systemu kontroli wersji")

print("a teraz szybka akcja reaktywacja")
print("no i wiadomość zwrotna, DOPBRZE CI IDZIE I OBY TAK DALEJ")
for i in range(0, 100):
  if i % 5 == 0:
    print("Liczby z przedaiłu od 0 do 100 podzielne przez 5:", i)
    
print("Dzisaiaj od nowa zabawa")
print("Jeszcze nie wiem czy mi sie uda")
