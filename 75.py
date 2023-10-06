from tkinter import *

class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

listaKontaktow = []

def dodajKontakt():
    imie = entry_Imie.get()
    nazwisko = entry_Nazwisko.get()
    telefon = entry_Telefon.get()
    email = entry_Email.get()

    kontakt = Kontakt(imie, nazwisko, telefon, email)
    listaKontaktow.append(kontakt)

    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0,END)
    entry_Telefon.delete(0,END)
    entry_Email.delete(0,END)

    entry_Imie.focus()

    pokazKontakty() #pokazuje listbox'a

    # print(listaKontaktow)

def pokazKontakty():
    listbox_ListaKontaktow.delete(0,END)
    for x, y in enumerate(listaKontaktow):
        listbox_ListaKontaktow.insert(x, f"{y.imie} {y.nazwisko}")

def usunKontakt():
    index = listbox_ListaKontaktow.index(ACTIVE)
    # print(index)
    listaKontaktow.pop(index)
    pokazKontakty()


def pokazSzczegoly():
    index = listbox_ListaKontaktow.index(ACTIVE)
    ob = listaKontaktow[index]
    label_rd3kropki1.config(text=ob.imie)
    label_rd3kropki2.config(text=ob.nazwisko)
    label_rd3kropki3.config(text=ob.telefon)
    label_rd3kropki4.config(text=ob.email)
    #label_rd3kropki1.config(text=listaKontaktow[index].email)


def edytujKontakt():
    index = listbox_ListaKontaktow.index(ACTIVE)
    ob = listaKontaktow[index]
    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Telefon.delete(0, END)
    entry_Email.delete(0, END)

    entry_Imie.insert(0, ob.imie)
    entry_Nazwisko.insert(0, ob.nazwisko)
    entry_Telefon.insert(0, ob.telefon)
    entry_Email.insert(0, ob.email)

    button_DodajKontakt.config(text="Zmien kontakt", command=zmienKontakt)

def zmienKontakt():
# pobierz index zaznaczonego kontaktu
    index = listbox_ListaKontaktow.index(ACTIVE)
    ob = listaKontaktow[index]

# pobierz z formularza: imie, nazwisko, telefon, email
    imie = entry_Imie.get()
    nazwisko = entry_Nazwisko.get()
    telefon = entry_Telefon.get()
    email = entry_Email.get()

# wyedytuj dane obiektu
    ob.imie = imie
    ob.nazwisko = nazwisko
    ob.telefon = telefon
    ob.email = email

# wyczysc pola formularza
    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Telefon.delete(0, END)
    entry_Email.delete(0, END)

# ustaw kursor na polu imie
    entry_Imie.focus()

# przywróc przycisk do ustawień pierwotnych
    button_DodajKontakt.config(text="Dodaj kontakt", command=dodajKontakt)

# odśwież listboxa
    pokazKontakty()


root = Tk()
root.geometry("700x300")
root.title("Książka telefoniczna")


ramkaLewa = Frame(root)
ramkaPrawa = Frame(root)
ramkaDolna = Frame(root)

ramkaLewa.grid(row=0, column=0, pady=(20, 30), padx=10)
ramkaPrawa.grid(row=0, column=1, sticky=N, pady=(20, 30), padx=10)
ramkaDolna.grid(row=1, column=0, columnspan=2,sticky=W, padx=10)

label_ListaKontaktow = Label(ramkaLewa, text="Lista kontaktów")
listbox_ListaKontaktow = Listbox(ramkaLewa, width=25, height=7)
button_PokazSzczegoly = Button(ramkaLewa, text="Pokaż szczegóły kontaktu", command=pokazSzczegoly)
button_UsunKontakt = Button(ramkaLewa, text="Usuń kontakt", command=usunKontakt)
button_EdytujKontakt = Button(ramkaLewa, text="Edytuj kontakt", command=edytujKontakt)

label_ListaKontaktow.grid(row=0, column=0, columnspan=3)
listbox_ListaKontaktow.grid(row=1, column=0, columnspan=3)
button_PokazSzczegoly.grid(row=2, column=0)
button_UsunKontakt.grid(row=2, column=1)
button_EdytujKontakt.grid(row=2, column=2)

label_NowyKontakt = Label(ramkaPrawa, text="Nowy kontakt")
label_Imie = Label(ramkaPrawa, text="Imie")
entry_Imie = Entry(ramkaPrawa)
label_Nazwisko = Label(ramkaPrawa, text="Nazwisko")
entry_Nazwisko = Entry(ramkaPrawa, width=30)
label_Telefon = Label(ramkaPrawa, text="Telefon")
entry_Telefon = Entry(ramkaPrawa)
label_Email = Label(ramkaPrawa, text="Email")
entry_Email = Entry(ramkaPrawa)
button_DodajKontakt = Button(ramkaPrawa,text="Dodaj kontakt", command=dodajKontakt)

label_NowyKontakt.grid(row=0, column=0, columnspan=2)
label_Imie.grid(row=1, column=0, sticky=W)
entry_Imie.grid(row=1, column=1, sticky=W)
label_Nazwisko.grid(row=2, column=0, sticky=W)
entry_Nazwisko.grid(row=2, column=1, sticky=W)
label_Telefon.grid(row=3, column=0, sticky=W)
entry_Telefon.grid(row=3, column=1, sticky=W)
label_Email.grid(row=4, column=0, sticky=W)
entry_Email.grid(row=4, column=1, sticky=W)
button_DodajKontakt.grid(row=5, column=0, columnspan=2)

label_SzczegolyKontaktu = Label(ramkaDolna, text="Szczegóły kontaktu")
label_rdImie = Label(ramkaDolna, text="Imie")
label_rd3kropki1 = Label(ramkaDolna, text="...", width=10)
label_rdNazwisko = Label(ramkaDolna, text="Nazwisko")
label_rd3kropki2 = Label(ramkaDolna, text="...", width=10)
label_rdTelefon = Label(ramkaDolna, text="Telefon")
label_rd3kropki3 = Label(ramkaDolna, text="...", width=10)
label_rdEmail = Label(ramkaDolna, text="Email")
label_rd3kropki4 = Label(ramkaDolna, text="...", width=10)

label_SzczegolyKontaktu.grid(row=0, column=0, columnspan=8, sticky=W)
label_rdImie.grid(row=1, column=0, sticky=W)
label_rd3kropki1.grid(row=1, column=1, sticky=W)
label_rdNazwisko.grid(row=1, column=2, sticky=W)
label_rd3kropki2.grid(row=1, column=3, sticky=W)
label_rdTelefon.grid(row=1, column=4, sticky=W)
label_rd3kropki3.grid(row=1, column=5, sticky=W)
label_rdEmail.grid(row=1, column=6, sticky=W)
label_rd3kropki4.grid(row=1, column=7, sticky=W)



button_PokazSzczegoly = Button(ramkaLewa, text="Pokaż szczegóły kontaktu")
button_UsunKontakt = Button(ramkaLewa, text="Usuń kontakt")
button_EdytujKontakt = Button(ramkaLewa, text="Edytuj kontakt")

root.mainloop()