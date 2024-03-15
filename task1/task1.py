#Sinu ülesanne:
# Kood saab inputina isikukoodi. Kood peab kontrollima:
#1) kas input koosneb ainult numbritest
#2) kas isikukoodil on õige pikkus

#Kood peab terminalis kuvama:
#1) sugu
#2) sünnipäev
#3) kus haiglas sündis
#4) kontrollkoodi

#Näide: 50102182738
#Mees
#2001 veebruar 18
#Tartu sünnitusmaja
#kontrollkood: 38

while True:
    isikukood = input("Teie isikukood: ")

    if isikukood.isdigit() and len(isikukood) == 11:
        print("Isikukood on 11 numbrit pikk")
        break
    else:
        print("Isikukood ei ole oige, palun sisestage isikukood uuesti!")

isik = [int(digit) for digit in isikukood]

if isik[0] == 3:
    print("Mees")
    aasta = "19"
elif isik[0] == 5:
    print("Mees")
    aasta = "20"
elif isik[0] == 4:
    print("Naine")
    aasta = "19"
elif isik[0] == 6:
    print("Naine")
    aasta = "20"

if isikukood[3:5] == "01":
    kuu = "jaanuar"
elif isikukood[3:5] == "02":
    kuu = "veebruar"
elif isikukood[3:5] == "03":
    kuu = "marts"
elif isikukood[3:5] == "04":
    kuu = "aprill"
elif isikukood[3:5] == "05":
    kuu = "mai"
elif isikukood[3:5] == "06":
    kuu = "juuni"
elif isikukood[3:5] == "07":
    kuu = "juuli"
elif isikukood[3:5] == "08":
    kuu = "august"
elif isikukood[3:5] == "09":
    kuu = "september"
elif isikukood[3:5] == "10":
    kuu = "oktoober"
elif isikukood[3:5] == "11":
    kuu = "november"
elif isikukood[3:5] == "12":
    kuu = "detsember"

print(aasta + isikukood[1:3] + " " + kuu + " " + isikukood[5:7])

if int(isikukood[7:10]) >= 1 and int(isikukood[7:10]) <= 10:
    print("Kuressaare haigla")
elif int(isikukood[7:10]) >= 11 and int(isikukood[7:10]) <= 19:
    print("Tartu Ülikooli Naistekliinik")
elif int(isikukood[7:10]) >= 21 and int(isikukood[7:10]) <= 150:
    print("Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)")
elif int(isikukood[7:10]) >= 151 and int(isikukood[7:10]) <= 160:
    print("Keila haigla")
elif int(isikukood[7:10]) >= 161 and int(isikukood[7:10]) <= 220:
    print("Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)")
elif int(isikukood[7:10]) >= 221 and int(isikukood[7:10]) <= 270:
    print("Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)")
elif int(isikukood[7:10]) >= 271 and int(isikukood[7:10]) <= 370:
    print("Maarjamõisa kliinikum (Tartu), Jõgeva haigla")
elif int(isikukood[7:10]) >= 371 and int(isikukood[7:10]) <= 420:
    print("Narva haigla")
elif int(isikukood[7:10]) >= 421 and int(isikukood[7:10]) <= 470:
    print("Pärnu haigla")
elif int(isikukood[7:10]) >= 471 and int(isikukood[7:10]) <= 490:
    print("Haapsalu haigla")
elif int(isikukood[7:10]) >= 491 and int(isikukood[7:10]) <= 520:
    print("Järvamaa haigla (Paide)")
elif int(isikukood[7:10]) >= 521 and int(isikukood[7:10]) <= 570:
    print("Rakvere haigla, Tapa haigla")
elif int(isikukood[7:10]) >= 571 and int(isikukood[7:10]) <= 600:
    print("Valga haigla")
elif int(isikukood[7:10]) >= 601 and int(isikukood[7:10]) <= 650:
    print("Viljandi haigla")
elif int(isikukood[7:10]) >= 651 and int(isikukood[7:10]) <= 700:
    print("Lõuna-Eesti haigla (Võru), Põlva haigla")

print("Kontrollkood: " + isikukood[10])