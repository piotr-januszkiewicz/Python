#PĘTLE I MODUŁY

import math
import random
import statistics
import keyword
import hello

#for
name = "Ted"
for character in name:
    print(character)

tv = ["Jaka to melodia",
      "Spadkobiercy",
      "Familiada"]
i=0
for element in tv:
    new = element
    new = new.upper()
    tv[i] = new
    i+=1
print(tv)

#to samo co powyżej ale z inną pętlą for
for i, show in enumerate(tv):
    new = tv[i]
    new = new.lower()
    tv[i] = new
print(tv)

for i in range(1, 16):
    print(i)

#while

x= 10
while x>0:
    x=x-2
    print(x)

#instrukcja break i continue
x = 100
while x>0:
    x-=1
    if x == 94:
        print("jest git")
        continue            #przeskoczy do następnej iteracji
    elif x == 90:
        print("koniec")
        break
    else:
        print(x)


#Tutaj są funkcjonalności modułów

numbers = [11,45,32,19,28,44,21,78,59,59]

print(math.pow(3,2))            #funkcja matematyczna : potęga
print(random.randint(0,100))    #losowa liczba
print(statistics.mean(numbers)) #średnia
print(statistics.median(numbers))#mediana
print(statistics.mode(numbers)) #dominanta

print(keyword.iskeyword("for"))
print(keyword.iskeyword("fortuna"))

hello.hello_world()

#R8
#Z1
print(statistics.harmonic_mean(numbers))
print(hello.cubed(3))











