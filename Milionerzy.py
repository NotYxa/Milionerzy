import random

print("""
---------------------------------------------------------------------------
███╗░░░███╗██╗██╗░░░░░██╗░█████╗░███╗░░██╗███████╗██████╗░███████╗██╗░░░██╗
████╗░████║██║██║░░░░░██║██╔══██╗████╗░██║██╔════╝██╔══██╗╚════██║╚██╗░██╔╝
██╔████╔██║██║██║░░░░░██║██║░░██║██╔██╗██║█████╗░░██████╔╝░░███╔═╝░╚████╔╝░
██║╚██╔╝██║██║██║░░░░░██║██║░░██║██║╚████║██╔══╝░░██╔══██╗██╔══╝░░░░╚██╔╝░░
██║░╚═╝░██║██║███████╗██║╚█████╔╝██║░╚███║███████╗██║░░██║███████╗░░░██║░░░
╚═╝░░░░░╚═╝╚═╝╚══════╝╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░
---------------------------------------------------------------------------
""")
imie = input("Witaj w Milionerach, wpisz swoję imie aby kontynuować: ")
pytania = {
    "Pierwsza kostka rubika powstała w: ": ["Polsce", "Węgrzech", "RPA", "Nie wiadomo została stworzona wiele wieków temu"],
    "Twórcą tego kodu jest: ": ["Święty Walenty", "Zenon Nakamura", "Jan III Sobieski", "Sir Carter"],
    "Ulubione anime Zenona to: ": ["JoJo", "One Piece", "Naruto", "Tokyo Revengers"],
    "Język użyty do napisania tego programu to: ": ["Java", "Python", "C#", "C++"],
    "Dumplings po angielsku to: ": ["Kawa", "Pierogi", "Kanapki", "Łysa głowa"],
    "Zenon ma urodziny: ": ["13 lipca", "25 września", "18 września", "18 lipca"],
    "Twoje imię to: ": ["Jan", imie, "Grzegorz", "Orzeł"],  
    "Rok rozpoczęcia IIWW to: ": ["1940", "1939", "1941", "1954"],
    "Karol Friz Wiśniewski to: ": ["Twój Stary", "Jupiter", "Agresor", "Anty Polak"],
    "Lewica jest: ": ["Mądra", "Głupia", "Cudowna", "Fajna"],
    "Kiedy odbył się D-day: ": ["1943", "1944", "1945", "1965"],
    "Warszawa to stolica: ": ["Francji", "Polski", "Rosji", "Kanady"]
    }

poprawne_odp = ["Węgrzech", "Zenon Nakamura", "One Piece", "Python", "Pierogi", "25 września", imie, "1939", "Jupiter", "Głupia", "1944", "Polski", "Węgrzech"]
lista_nagrod = [0, 100, 250, 500, 1000, 2500, 5000, 10000, 50000, 100000, 250000, 500000, 1000000]
licznik_nagrody = 0
licznik_pytan = 0
losowe_pytania = {}

granie = input("Będziemy teraz zadawać pytania, czy jesteś gotowy? (tak = 1/nie = 0)")

while licznik_nagrody < 13 or granie:
    if granie == "1":
        for pytanie, odpowiedzi in pytania.items():
            random.shuffle(odpowiedzi)
            pytanie_z_odp = {pytanie: odpowiedzi}
            losowe_pytania.update(pytanie_z_odp)
            
        for pytanie, odpowiedzi in losowe_pytania.items():
            odp = 0
            odp_litera = input(pytanie + "A. " + odpowiedzi[0] + " B. " + odpowiedzi[1] + " C. " + odpowiedzi[2] + " D. " + odpowiedzi[3] + " (Napisz A/B/C/D)")

            while odp == 0:
                if odp_litera == "A":
                    odp = odpowiedzi[0]
                elif odp_litera == "B":
                    odp = odpowiedzi[1]
                elif odp_litera == "C":
                    odp = odpowiedzi[2]
                elif odp_litera == "D":
                    odp = odpowiedzi[3]
                else:
                   odp_litera = input("Napisz ponownie znak. (A/B/C/D)")
                   
            if odp == poprawne_odp[licznik_pytan]:
                print("Poprawna odpowiedź!")
                licznik_nagrody += 1
                licznik_pytan += 1
                print("Twoja aktualna nagroda to " + str(lista_nagrod[licznik_nagrody]) + "$.")
            else:
                print("Przegrałeś!")
                granie = 2.115
                break
            
    if licznik_nagrody >= 12:
        print("Wygrałeś stałeś się milionerem!")
    if granie == 2.115:
        print("Następnym razem się uda :(")
        break
    else:
        granie = input("Gdy będziesz gotowy na grę napisz \"1\".")
    


        

