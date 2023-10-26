from turtle import *
import turtle_figure

def dec_to_bin(carre_size):
    write_read = input('Voulez vous ajouter (a) ou lire (l) :')
    if write_read.lower() == "a":
        with open('db.txt', 'a') as db:
            str_dec = input('Nombre décimal a transformé en binaire :')
            int_dec = int(str_dec)
            nb_bin = str(bin(int_dec))[2:]
            print(nb_bin)
            db.write(f"{nb_bin}\n")
        return "Write"
    elif write_read.lower() == "l":
        with open('db.txt', 'r') as db:
            bgcolor('grey')
            up()
            goto(-250, 250)
            texte = db.read()
            lignes = texte.split("\n")
            for ligne in lignes:
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
                    up()
                    bk(carre_size / 2)
                    rt(90)
                    fd(carre_size / 2)
                    lt(90)
                up()
                lt(90)
                fd(len(ligne) * carre_size)
                rt(90)
                nb = 2
                fd(nb * carre_size)
            ht()
            exitonclick()
        return "Read"
        
dec_to_bin(30)