#PLIKI
import os
import csv

os.path.join("Users","piotr","Desktop","python","newFile.txt")

#proste otwieranie pliku
st = open("st.txt", "w")
st.write("Hello file!")
st.close()

#otwarcie i automatyczne zamknięcie pliku po wykonaniu operacji
with open("st.txt","w") as file:
    file.write("Hello file! how it's going")

#czytanie wartości z pliku
my_list = []
with open("st.txt","r") as file:
    my_list.append(file.read())

print(my_list)

with open("newFile.csv", "w", newline = '') as file:
    write = csv.writer(file,delimiter=",")
    write.writerow(["jeden","dwa","trzy"])
    
#R9
#Z1
with open("Presentation to speak.txt","r") as file:
    print(file.read())

#Z2
print ("Jak masz na imię?")
odpowiedź = []
odpowiedź = input()
with open("autoprezentacja.txt", "w") as file:
    file.write(odpowiedź)
    
#Z3 #TODO nie działa z polskimi znakami
mylist = [["Top Gun", "Ocean's Eleven", "Raport mniejszosci"], ["Titanic", "Ostatni Jedi",
"Incepcja"],["Pulp Fiction", "Czlowiek w ogniu", "Seksmisja"]]
with open ("films.csv","w+",newline = '') as file:
    write = csv.writer(file,delimiter=",")
    write.writerows(mylist)
print(mylist)




