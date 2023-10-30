from turtle import *
import turtle_figure

def mouvement_bit_colonne(carre_size):
    up()
    bk(carre_size / 2)
    rt(90)
    fd(carre_size / 2)
    lt(90)

def mouvement_bit_ligne(carre_size):
    up()
    rt(90)
    bk(carre_size / 2)
    lt(90)
    fd(carre_size / 2)

def mouvement_bit_ligne_2(carre_size):
    up()
    rt(90)
    bk(carre_size / 2)
    lt(90)
    fd(carre_size / 2 + carre_size)
    
def mouvement_bit_ligne_3(carre_size):
    up()
    rt(90)
    bk(carre_size / 2)
    lt(90)
    fd(carre_size / 2)
    # rt(180)

def mouvement_nb_colonne(ligne, carre_size):
    up()
    lt(90)
    fd(len(ligne) * carre_size)
    rt(90)
    nb = 2
    fd(nb * carre_size)

def mouvement_nb_ligne(ligne, carre_size):
    up()
    lt(180)
    fd(len(ligne) * carre_size)
    lt(90)
    nb = 2
    fd(nb * carre_size)
    lt(90)

def mouvement_nb_ligne_2(ligne, carre_size):
    up()
    fd(len(ligne) * carre_size)
    rt(90)
    nb = 2
    fd(nb * carre_size)
    lt(90)   
    
def mouvement_nb_ligne_3(carre_size):
    up()
    rt(90)
    nb = 2
    fd(nb * carre_size)
    lt(90)  






def dec_to_bin(carre_size):
    # write_read = input('Voulez vous ajouter (a) ou lire (l) :')
    write_read = "l"
    if write_read.lower() == "a":
        with open('db.txt', 'a') as db:
            str_dec = input('Nombre décimal a transformé en binaire :')
            int_dec = int(str_dec)
            nb_bin = str(bin(int_dec))[2:]
            print(nb_bin)
            db.write(f"{nb_bin}\n")
        return "Write"
    elif write_read.lower() == "l":
        # align_item = input("Alignement colonne (c), ligne (l): ")
        align_item = "c"
        with open('db.txt', 'r') as db:
            bgcolor('grey')
            up()
            if align_item == "c":
                goto(-250, 250)
            elif align_item == "l":
                goto(250, 250)
            
            texte = db.read()
            lignes = texte.split("\n")
            lignes = [ligne for ligne in lignes if ligne != ""]
            for ligne in lignes:
                down()
                write(int("0b" + ligne, base=2))
                if align_item == "l":
                    # reversed(ligne)
                    up()
                    bk(len(ligne) * carre_size)
                    down()
            
                for bit in ligne:
                    if int(bit) == 0:
                        turtle_figure.carre(carre_size, "white", "black", 0)
                        print(0)
                    elif int(bit) == 1:
                        turtle_figure.carre(carre_size, "black", "white", 1)
                        print(1)
                    else:
                        print(f"erreur le nombre ({ligne}) n'est pas en binaire")
                    if align_item == "c":
                        mouvement_bit_colonne(carre_size)
                    elif align_item == "l":
                        mouvement_bit_ligne_3(carre_size)
                if align_item == "c":
                    mouvement_nb_colonne(ligne, carre_size)
                elif align_item == "l":
                    mouvement_nb_ligne_3(carre_size)
            ht()
            exitonclick()
        return "Read"
        
dec_to_bin(30)