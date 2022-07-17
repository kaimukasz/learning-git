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

print("\n")

# ZADANIE 2
# Część 1
# Sposób 1
print("ZADANIE 2\n\nCzęść 1\nSposób 1\n")
for i in range(0, 100):
  if i % 5 == 0:
    print(f"Liczby podzielne przez 5 z zakresu od 0 do 100 {i}")

print("\n\n")

# Sposób 2
print("Sposób 2\n")
divisible = [i for i in range(0, 100) if i % 5 == 0]
print(f"Liczby podzielne przez 5 z zakresu o 0 do 100 to {divisible}")

print("\n\n")

# Część 2
print("Część 2\n")
exponentiation = [j * j * j for j in divisible]
print(f"Liczby podniesione do potęgi 3 spośród liczb podzielnych przez 5 to {exponentiation}")