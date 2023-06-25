import sqlite3
from sqlite3 import Error

class Turisticka_agencija():
    def __init__(self, id):
        self.id = id


class Putnik(Turisticka_agencija):

    def __init__(self, id, jmbg, ime, prezime):
        Turisticka_agencija.__init__(self, id)
        self.jmbg = jmbg
        self.ime = ime
        self.prezime = prezime

    def __str__(self):
        return "Jmbg putnika: " + str(self.jmbg) + ", ime putnika: " \
            + self.ime + ", prezime putnika: " + self.prezime

class Ponuda(Turisticka_agencija):

    def __init__(self, id, broj_ponude, destinacija, broj_dana, cijena):
        Turisticka_agencija.__init__(self, id)
        self.broj_ponude = broj_ponude
        self.destinacija = destinacija
        self.broj_dana = broj_dana
        self.cijena = cijena

    def __str__(self):
        return "Broj ponude: " + str(self.broj_ponude) + ", destinacija: " \
            + self.destinacija + ", broj dana boravka: " + str(self.broj_dana) + ", cijena: " + str(self.cijena)

class Osiguranje(Turisticka_agencija):

    def __init__(self, id, broj, naziv, osiguranje):
        Turisticka_agencija.__init__(self, id)
        self.broj = broj
        self.naziv = naziv
        self.osiguranje = osiguranje

    def __str__(self):
        return "Broj osiguranja: " + str(self.broj) + ", naziv osiguranja: " + self.naziv \
            + ", putnik je osiguran: " + self.osiguranje

class Vrstauplate(Turisticka_agencija):

    def __init__(self, id, broj_licne, vrsta, placeno, datum):
        Turisticka_agencija.__init__(self, id)
        self.broj_licne_karte = broj_licne
        self.vrsta_uplate = vrsta
        self.placeno = placeno
        self.datum = datum

    def __str__(self):
        return "Broj lične karte putnika: " + self.broj_licne_karte + ", vrsta uplate: " + self.vrsta_uplate \
            + ", plaćeno: " + self.placeno + ", datum uplate: " + self.datum


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)

def create_putnik(conn, putnik):
    try:
        sql = """ INSERT INTO putniks(ime, prezime)
                 VALUES(?, ?) """
        cur = conn.cursor()
        params = (putnik.ime, putnik.prezime)
        cur.execute(sql, params)
        conn.commit()
    except Error as e:
        print(e)

def update_putnik(conn):
    cursor = conn.cursor()
    cursor.execute(""" UPDATE putniks SET ime = "Darija" WHERE prezime = "Dacaa"; """)
    conn.commit()

def delete_putnik(conn):
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM putniks WHERE prezime = "ĐURICA"; """)
    conn.commit()

def select_all_putnik(conn):
    sql = """ SELECT * FROM putniks; """
    cur = conn.cursor()
    cur.execute(sql)
    ans = cur.fetchall()
    return ans

if __name__ == "__main__":
    sql_create_putnik_table = """ CREATE TABLE IF NOT EXISTS putniks (
                                  jmbg integer PRIMARY KEY,
                                  ime text NOT NULL,
                                  prezime text NOT NULL); """
    conn = create_connection("../putnik.db")

    if conn is not None:
        create_table(conn, sql_create_putnik_table)

        while True:
            izbor = int(input("Unesite 0 za kraj programa, 1 za unos novog putnika, 2 za update putnika, 3 za brisanje putnika, 4 za ispis svih putnika: "))
            if izbor == 0:
                break
            elif izbor == 1:
                id = int(input("Unesite ID agencije: "))
                jmbg = int(input("Unesite JMBG putnika: "))
                ime = input("Unesite ime putnika: ")
                prezime = input("Unesite prezime putnika: ")
                put = Putnik(id, jmbg, ime, prezime)
                create_putnik(conn, put)
            elif izbor == 2:
                u = update_putnik(conn)
            elif izbor == 3:
                d = delete_putnik(conn)
            elif izbor == 4:
                rputnik = select_all_putnik(conn)
                for i in rputnik:
                    print(i)
    else:
        print("Error.")


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)

def create_ponuda(conn, ponuda):
    try:
        sql = """ INSERT INTO ponudas(destinacija, broj_dana, cijena)
                 VALUES(?, ?, ?) """
        cur = conn.cursor()
        params = (ponuda.destinacija, ponuda.broj_dana, ponuda.cijena)
        cur.execute(sql, params)
        conn.commit()
    except Error as e:
        print(e)

def update_ponuda(conn):
    cursor = conn.cursor()
    cursor.execute(""" UPDATE ponudas SET destinacija = "Madrid" WHERE broj_dana = 3; """)
    conn.commit()

def delete_ponuda(conn):
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM ponudas WHERE broj_dana = "5"; """)
    conn.commit()

def select_all_ponuda(conn):
    sql = """ SELECT * FROM ponudas; """
    cur = conn.cursor()
    cur.execute(sql)
    ans = cur.fetchall()
    return ans

if __name__ == "__main__":
    sql_create_ponuda_table = """ CREATE TABLE IF NOT EXISTS ponudas (
                                  broj_ponude integer PRIMARY KEY,
                                  destinacija text NOT NULL,
                                  broj_dana integer NOT NULL,
                                  cijena integer NOT NULL); """
    conn = create_connection("../ponuda.db")

    if conn is not None:
        create_table(conn, sql_create_ponuda_table)

        while True:
            izbor = int(input("Unesite 0 za kraj programa, 1 za unos nove ponude, 2 za update ponude, 3 za brisanje ponude, 4 za ispis svih ponuda: "))
            if izbor == 0:
                break
            elif izbor == 1:
                id = int(input("Unesite ID agencije: "))
                br_ponude = int(input("Unesite broj ponude: "))
                dest = input("Unesite destinaciju ponude: ")
                br_dana = int(input("Unesite broj dana boravka: "))
                cijena = float(input("Unesite cijenu boravka: "))
                p = Ponuda(id, br_ponude, dest, br_dana, cijena)
                create_ponuda(conn, p)
            elif izbor == 2:
                u = update_ponuda(conn)
            elif izbor == 3:
                d = delete_ponuda(conn)
            elif izbor == 4:
                rponuda = select_all_ponuda(conn)
                for i in rponuda:
                    print(i)
    else:
        print("Error.")


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)

def create_osiguranje(conn, osiguranje):
    try:
        sql = """ INSERT INTO osiguranjes(naziv, osiguranje)
                 VALUES(?, ?) """
        cur = conn.cursor()
        params = (osiguranje.naziv, osiguranje.osiguranje)
        cur.execute(sql, params)
        conn.commit()
    except Error as e:
        print(e)

def update_osiguranje(conn):
    cursor = conn.cursor()
    cursor.execute(""" UPDATE osiguranjes SET naziv = "Winner" WHERE osiguranje = "ds"; """)
    conn.commit()

def delete_osiguranje(conn):
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM osiguranjes WHERE osiguranje = "DA"; """)
    conn.commit()

def select_all_osiguranje(conn):
    sql = """ SELECT * FROM osiguranjes; """
    cur = conn.cursor()
    cur.execute(sql)
    ans = cur.fetchall()
    return ans

if __name__ == "__main__":
    sql_create_osiguranje_table = """ CREATE TABLE IF NOT EXISTS osiguranjes (
                                  broj integer PRIMARY KEY,
                                  naziv text NOT NULL,
                                  osiguranje text NOT NULL); """
    conn = create_connection("../osiguranje.db")

    if conn is not None:
        create_table(conn, sql_create_osiguranje_table)

        while True:
            izbor = int(input("Unesite 0 za kraj programa, 1 za unos novog osiguranje, 2 za update osiguranja, 3 za brisanje osiguranja, 4 za ispis svih osiguranja: "))
            if izbor == 0:
                break
            elif izbor == 1:
                id = int(input("Unesite ID agencije: "))
                br_osiguranja = int(input("Unesite broj osiguranja: "))
                naziv = input("Unesite naziv osiguranja: ")
                osig = input("Da li je putnik osiguran (da/ne): ")
                os = Osiguranje(id, br_osiguranja, naziv, osig)
                create_osiguranje(conn, os)
            elif izbor == 2:
                u = update_osiguranje(conn)
            elif izbor == 3:
                d = delete_osiguranje(conn)
            elif izbor == 4:
                rosiguranje = select_all_osiguranje(conn)
                for i in rosiguranje:
                    print(i)
    else:
        print("Error.")


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)

def create_vrstauplate(conn, vrstauplate):
    try:
        sql = """ INSERT INTO vrstauplates(vrsta_uplate, placeno, datum)
                 VALUES(?, ?, ?) """
        cur = conn.cursor()
        params = (vrstauplate.vrsta_uplate, vrstauplate.placeno, vrstauplate.datum)
        cur.execute(sql, params)
        conn.commit()
    except Error as e:
        print(e)

def update_vrstauplate(conn):
    cursor = conn.cursor()
    cursor.execute(""" UPDATE vrstauplates SET vrsta_uplate = "gotovina" WHERE placeno = "-"; """)
    conn.commit()

def delete_vrstauplate(conn):
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM vrstauplates WHERE placeno = "DA"; """)
    conn.commit()

def select_all_vrstauplate(conn):
    sql = """ SELECT * FROM vrstauplates; """
    cur = conn.cursor()
    cur.execute(sql)
    ans = cur.fetchall()
    return ans

if __name__ == "__main__":
    sql_create_vrstauplate_table = """ CREATE TABLE IF NOT EXISTS vrstauplates (
                                  broj_licne_karte integer PRIMARY KEY,
                                  vrsta_uplate text NOT NULL,
                                  placeno text NOT NULL,
                                  datum text NOT NULL); """
    conn = create_connection("../vrstauplate.db")

    if conn is not None:
        create_table(conn, sql_create_vrstauplate_table)

        while True:
            izbor = int(input("Unesite 0 za kraj programa, 1 za unos nove uplate, 2 za update uplate, 3 za brisanje uplate, 4 za ispis svih uplata: "))
            if izbor == 0:
                break
            elif izbor == 1:
                id = int(input("Unesite ID agencije: "))
                br_lk = input("Unesite broj lične karte: ")
                vrsta = input("Unesite vrstu uplate (kartica/gotovina): ")
                placeno = input("Unesite da li je putnik uplatio (da/ne): ")
                datum = input("Unesite datum uplate (d. m. g.): ")
                vu = Vrstauplate(id, br_lk, vrsta, placeno, datum)
                create_vrstauplate(conn, vu)
            elif izbor == 2:
                u = update_vrstauplate(conn)
            elif izbor == 3:
                d = delete_vrstauplate(conn)
            elif izbor == 4:
                rvrstauplate = select_all_vrstauplate(conn)
                for i in rvrstauplate:
                    print(i)
    else:
        print("Error.")


print("---------------------------------------------------------------")
provjera = int(input("Unesite redni broj da biste vidjeli putnika i njegove izabrane podatke o putovanju: "))
print(" ")

conn = sqlite3.connect("../putnik.db")
cur = conn.cursor()
cur.execute(""" SELECT * FROM putniks; """)
svi_putnici = cur.fetchall()
for m in svi_putnici:
    id_value = m[0]
    if m[0] == provjera:
        print(m)
        conn = sqlite3.connect("../ponuda.db")
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM ponudas; """)
        sve_ponude = cur.fetchall()
        for n in sve_ponude:
            id_value = n[0]
            if n[0] == m[0]:
                print(n)
                conn = sqlite3.connect("../osiguranje.db")
                cur = conn.cursor()
                cur.execute(""" SELECT * FROM osiguranjes; """)
                sva_osiguranja = cur.fetchall()
                for k in sva_osiguranja:
                    id_value = k[0]
                    if k[0] == n[0]:
                        print(k)
                        conn = sqlite3.connect("../vrstauplate.db")
                        cur = conn.cursor()
                        cur.execute(""" SELECT * FROM vrstauplates; """)
                        sve_uplate = cur.fetchall()
                        for l in sve_uplate:
                            id_value = l[0]
                            if l[0] == k[0]:
                                print(l)