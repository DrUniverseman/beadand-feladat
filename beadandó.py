#Nagy Sebestyén János(AOK1O5)

from datetime import datetime


class Szoba:
    def __init__(self, szobsz, ar):
        self.szobsz = szobsz
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobsz, bath):
        super().__init__(szobsz, 70000)
        self.bath = bath

class KetagyasSzoba(Szoba):
    def __init__(self, szobsz, extra):
        super().__init__(szobsz, 90000)
        self.extra = extra

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.fgs_ok = []


    def add_szoba(self, szoba):
        self.szobak.append(szoba)


    
    def fgs(self, szobsz, datum):
        for fgs in self.fgs_ok:
            if fgs.szoba.szobsz == szobsz and fgs.datum == datum:
                print("\nA szoba már foglalt ezen a napon. \nVálasszon másik szobát vagy másik dátumot!")
                return
        for szoba in self.szobak:
            if szoba.szobsz == szobsz:
                self.fgs_ok.append(Foglalas(szoba, datum))
                print("Sikeres foglalás!")
                return szoba.ar
        print("\nA megadott szobaszám nincs a szállodában.")

    def lmond(self, szobsz, datum):
        for fgs in self.fgs_ok:
            if fgs.szoba.szobsz == szobsz and fgs.datum == datum:
                self.fgs_ok.remove(fgs)
                return True
        return False
    
    def list_fgs_ok(self):
        for fgs in self.fgs_ok:
            print(f"Szoba: {fgs.szoba.szobsz}, Időpont: {fgs.datum}")


hotel = Szalloda("Pihenő Hotel")


hotel.add_szoba(EgyagyasSzoba("12","Kád"))
hotel.add_szoba(EgyagyasSzoba("14","Zuhany"))
hotel.add_szoba(KetagyasSzoba("13","Jacuzzi"))


hotel.fgs("12", datetime(2024, 7, 21))
hotel.fgs("14", datetime(2024, 7, 23))
hotel.fgs("13", datetime(2024, 7, 27))
hotel.fgs("12", datetime(2024, 7, 27))
hotel.fgs("14", datetime(2024, 7, 27))


while True:

    print("\nVálassz műveletet:")
    print("1. Szoba foglalás")
    print("2. Foglalás lemondás")
    print("3. Foglalás listázás")
    print("4. Szoba listázás")
    print("5. Kilépés")
    case = input("Művelet kiválasztás(1;2;3;4;5): ")

    if case == "1":
        szobsz = input("\nAdd meg a foglalandó szoba számát: ")
        datum = input("Add meg a foglalás dátumát(év-hónap-nap, csak egy napra lehetséges a foglalás): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("\nHibás dátum! A foglalás csak jövőbeli időpontra lehetséges.")
            else:
                ar = hotel.fgs(szobsz, datum)
                if ar:
                    print(f"A foglalás megtörtént! Ára: {ar} Ft")
                else:
                    print("\nHibás szobaszám!")
        except ValueError:
            print("\nHibás dátum forma!")
    elif case == "2":
        szobsz = input("\nAdd meg a lemondandó foglalás szoba számát: ")
        datum = input("Add meg a lemondandó foglalás dátumát(év-hónap-nap): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            siker = hotel.lmond(szobsz, datum)
            if siker:
                print("\nA foglalás le lett lemondva.")
            else:
                print("\nNincs ilyen foglalás.")
        except ValueError:
            print("\nHibás dátum forma!")
    elif case == "3":
        hotel.list_fgs_ok()
    elif case == "4":
            print("Szobák száma:")
            print(len(hotel.szobak))
            print("Egyágyas szobák:")
            for szoba in hotel.szobak:
                if isinstance(szoba, EgyagyasSzoba):
                    print(f"Szoba száma: {szoba.szobsz}, Ára: {szoba.ar} Ft, (Fürdő: {szoba.bath})")
            print("\nKétágyas szobák:")
            for szoba in hotel.szobak:
                if isinstance(szoba, KetagyasSzoba):
                    print(f"Szoba száma: {szoba.szobsz}, Ára: {szoba.ar} Ft, (Extra: {szoba.extra})")
    elif case == "5":
        break
    else:
        print("\nHibás választás!")