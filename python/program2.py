print("""ile
wierszy
tu
widać?
""")

string = "onomatopeja"
#od początku do końca
print(string[0])
print(string[1])
print(string[2])

#od końca do początku
print(string[-1])
print(string[-2])
print(string[-3])

#konkatenacja
space = ' '
kot = "kot"
w = 'w'
butach = "BUTACH"
print(kot+space+w+space+butach)

#UPPER, lower, Capitalize
print(kot.upper())
print(butach.lower())
print(kot.capitalize())

print("kot {} {}".format(w,butach.lower()))

#dzielenie łańcucha znaków na części wg. klucza podanego jako argument funkcji split()
print("Hej.Cześć.Siema!".split("."))

#wstawianie znaku '.' między każdy znak z łańcucha 
abc = "abcdefghijklmnop"
newabc=".".join(abc)
print(newabc)

#usuwanie znaków białych 
word = "           hello          "
print(word.strip())

word1 = "Szumią lasy na gór szczycie szumią sobie w dal"
word1 = word1.replace("z","8")
print(word1)

#pokazuje index pierwszego znalezionego znaku łańcucha określonego przez argument
print(word1.index("ó"))
#uwaga na ValueError: występuje gdy nie znajdzie znaku

#substring 
print("lasy" in word1) #True
print("losy" in word1) #False

print("specjalne znaki np. \"cudzysłów\" poprzedzamy znakiem \"\ \"")

numbers = ["1",
           "2",
           "3",
           "4",
           "5"]
print(numbers[0:3]) #['1', '2', '3']

#R6
#Z1
Camus = "Camus"
print(Camus[0])
print(Camus[1])
print(Camus[2])
print(Camus[3])
print(Camus[4])

#Z2
napis = "Wczoraj napisałem {} i wysłałem do {}".format("maila", "Basi")
print(napis)

#Z3
print("aldous Huxley urodził się w 1894 roku.".capitalize())

#Z4
print("Gdzie teraz? Kto teraz? Kiedy, teraz?".split("?"))

#Z5
słowo = ["Zwinny", "lis", "przeskoczył", "nad", "leniwym", "psem", "."]

#TODO 5-10 strona 93

           







