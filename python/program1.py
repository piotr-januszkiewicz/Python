#LIST

lis = list()
fruit = ["banan", "jabłko", "pomidor"]
print(fruit)

fruit.append("pomarańcza")
print(fruit)

random_objects = ["banan"]
random_objects.append(1.1111)
random_objects.append(0)
random_objects.append(True)
print(random_objects)
print(random_objects[1])

random_objects[2]="Witaj świecie"
print(random_objects)

popped_object = random_objects.pop()
print(popped_object)
print(random_objects)

random_objects = random_objects + fruit
print(random_objects)

if "jabłko" in random_objects:
    print("jabłko jest w liście random_objects")
if "kur" not in random_objects:
    print("kur nie ma w random_objects")

print(len(random_objects))

#KROTKI (TUPLES)
tupl = tuple()
#to jest krotka
tup = ("hey",)
#to nie jest krotka
ntup = ("hey")
#Zawartości krotek nie można modyfikować. Poza tym można sprawdzić jej elementy itp.

#SŁOWNIK
#tworzony parami klucz-wartość (odwzorowywanie)
dictionary1 = dict()
dictionary2 = {"first" : "ja", "second" : "ty", "hotel" : "trivago"}
print(dictionary2)

#dodawanie nowych wartości
dictionary2["programowanie"] = "zabawa"
dictionary2["bitwa pod grunwaldem"] = 1410
print(dictionary2)
print(dictionary2["bitwa pod grunwaldem"])

if "first" in dictionary2:
    print("ja ja")
print("hotel" in dictionary2)

#Kontenery w kontenerach
lista_gatunków_gier = list()
rpg = ["wiedźmin ", "fallout", "skyrim"]
akcja = ["far cry", "broforce", "CS:GO"]
taktyczne = ["tropico", "anno", "HOMM"]

lista_gatunków_gier.append(rpg)
lista_gatunków_gier.append(akcja)
lista_gatunków_gier.append(taktyczne)

print(lista_gatunków_gier[0][1])

#SUMMARY
#krotka kiedy nie zmieniają nam się wartości: reprezentacja stałych
#lista kiedy chcemy uporządkowany zestaw obiektów, lub po prostu obiekty
#słownik kiedy mamy parę klucz-wartość np. pytanie w ankiecie i odpowiedź

#R5
#Z1
muzycy = ["Skillet",
          "Linkin Park",
          "A7x",
          "Queen"]
print(muzycy)

#Z2
współ_geog = list()
lubiatowo = ("54°47′44", "17°51′56″")
katowice = ("50°15′51″", "19°01′25″")
współ_geog.append(lubiatowo)
współ_geog.append(katowice)
print(współ_geog)

#Z3
pioter = dict()
pioter["wzrost"] = 180
pioter["waga"] = 90
pioter["ulubiony kolor"] = "czerwony"
pioter["palacz"] = False
print(pioter)

#Z4
x=input("co chcesz o mnie wiedziec? ")
if x in pioter:
    print(pioter[x])
else: print("Nie znaleziono")
        
#Z5
muzycy = dict()
Skillet = ["Save me",
           "Rebirthing",
           "Not gonna die",
           "Comatose",
           "The resistance",
           "Yours to hold"]
A7x = ["Nightmare",
       "A little piece of heaven",
       "Seize the day",
       "Dear God",
       "So far away",
       "Blinded in chains"]
gunsNroses = ["Sweet child o mine",
              "November rain",
              "My Michelle",
              "Paradise city"]
muzycy["Skillet"] = Skillet
muzycy["A7x"] = A7x
muzycy["Guns n Roses"] = gunsNroses
print(muzycy)















