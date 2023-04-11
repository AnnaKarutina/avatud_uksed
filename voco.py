from tkinter import *
from tkinter import colorchooser

# joonistame tkinteri abil
raam = Tk()

# ja kõike teostamiseks on hulk abifunktsioone

# 1 - funktsioon, mis kutsutakse kui värv ei ole it kooli värv
def teade_akken(teade_sõnum):
    # loome akken, mis on peale voco akna
   teade = Toplevel(raam)
    # keelame akna suuruse muutmist
   teade.resizable(False, False)
    # määrame akna suurust laius x kõrgus
   teade.geometry("750x250")
    # määrame aknale pealkiri
   teade.title("Tähtis teade")
   # loome teks, mis kuvatakse
   Label(teade, text=teade_sõnum, font=('Montserrat 17 bold')).pack(padx = 30, pady = 30)
    # lisame nupp, mis paneb akken kinni
   ok_nupp = Button(teade, text="OK", font=('Montserrat 14'), command=raam.destroy)
    # kuvame nupp
   ok_nupp.pack(pady = 30)

# 2 - funktsioon, mis kutsutakse värvi nuppu klikkimisel
def vali_värv():
    # värv on salvestatud hex koodina
    valitud_värv = colorchooser.askcolor(title="Choose color")[1]
    # prindime sinu jaoks valitud värvi väärtus ja selgitame, mis edasi saab
    print(">>>>\nVärv, mis sa valisid on " + valitud_värv + ".\nMärkasid, et sellisel kujul värvi kuskil ei näidata?\nKOHE KÕIK SELGITAME SULLE\n>>>>")
    # kui värv ei ole sobilik,
    if (valitud_värv != "#20c4f4"):
        teade_akken("Tundub, et antud kood ei ole päris õige.\nSoovitan vaadata lähemalt programmi koodi,\n äkki seal peidub vastus?") # siis kuvatakse teade vihjega
    else:
        # muidu üks voco tähtedest värvitakse õige värviga
        tahvel.create_oval(250, 70, 460, 280, fill=valitud_värv, outline=valitud_värv)
        teade_akken("Super, oled murdnud VOCO koodi!") # ja kuvatakse teade õnnestumise kohta

# 3 - voco kuvamine
def voco():
    # joonistamine on koordinaatide põhine - tasand on vasakust ülanurgast alates paremale ja alla
    # mustade servadega must kolmnurk
    tahvel.create_polygon(40, 80, 260, 80, 150, 270, fill="#000000", outline="#000000")
    # must ring
    tahvel.create_oval(250, 70, 460, 280, fill="#000000", outline="#000000")
    # must ring
    tahvel.create_oval(250, 300, 460, 500, fill="#000000", outline="#000000")
    # valge servadega valge kolmnurk
    tahvel.create_polygon(500, 240, 360, 400, 500, 520, fill="#FFFFFF", outline="#FFFFFF")
    # must ring
    tahvel.create_oval(440, 300, 650, 500, fill="#000000", outline="#000000")

# põhiprogramm
if __name__ == '__main__':
    # määrame aknale nimi
    raam.title("VOCO koolid")
    # keelame akna suuruse muutmist
    raam.resizable(False, False)
    # loome tahvli laiusega 1000px
    tahvel = Canvas(raam, width=710, height=600, background="white")
    # loome nupp ja lisame nuppule värvivaliku käivitamine
    button = Button(tahvel, text="Murra VOCO koodi", font=('Montserrat 14'), command=vali_värv)
    # paigutame nupp tahvlile
    button.place(x = 170, y = 5, width = 250)
    # joonistame voco
    voco()
    # paigutame tahvli raami ja teeme nähtavaks
    tahvel.pack()
    # siseneme põhitsüklisse
    raam.mainloop()