from app import path
import os
from PIL import Image
import zpl
from datetime import date


class Biglietto():
    
    def __init__(self, numero, data_ins, data_ext=""):
        self.numero = numero
        self.data_inserimento = data_ins
        self.data_estrazione = data_ext

    def toCsv(self):
        return '{},{},{}\n'.format(self.numero, self.data_inserimento, self.data_estrazione)

    def __repr__(self):
        return 'Numero: {} - Data inserimento: {} - Data estrazione: {}\n'.format(self.numero, self.data_inserimento, self.data_estrazione)

    def printZebra(self):
        l = zpl.Label(60,60)

        l.origin(0,20)
        l.write_text(str(self.numero), char_height=10, char_width=8, line_width=60, justification='C')
        l.endorigin()

        l.preview()


def select_all():
    with open(path) as f:
        content = f.readlines()
    res_list = []
    for line in content:
        value, data_ins, data_ext = line.split(",")
        if data_ext == "\n":
            res_list.append(Biglietto(value, data_ins, data_ext))
    return res_list


def delete(biglietto:Biglietto):
    with open(path, "r") as f:
        content = f.readlines()
    with open(path, "w") as f:
        for line in content:
            value, _, _ = line.split(",")
            if value != biglietto.numero:
                f.write(line)
            else:
                biglietto.data_estrazione = date.today()
                f.write('{},{},{}\n'.format(biglietto.numero, biglietto.data_inserimento, biglietto.data_estrazione))

 
def insert(biglietto:Biglietto):
    f = open(path, "a")
    f.write(biglietto.toCsv())
    f.close() 

if __name__=="__main__":
    my_list = select_all()
    print(my_list)
    my_ticket = my_list[0]
    delete(my_ticket)