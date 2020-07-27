from app import path
import os
from PIL import Image
import zpl


class Biglietto():
    
    def __init__(self, numero):
        self.numero = numero

    def __repr__(self):
        return '{}\n'.format(self.numero)

    def printZebra(self):
        l = zpl.Label(60,60)

        l.origin(0,20)
        l.write_text(str(self.numero), char_height=10, char_width=8, line_width=60, justification='C')
        l.endorigin()

        l.preview()


def select_all():
    with open(path) as f:
        content = f.readlines() 
    return [Biglietto(int(x.strip())) for x in content if x.strip() != ""]


def delete(biglietto:Biglietto):
    with open(path, "r") as f:
        content = f.readlines()
    with open(path, "w") as f:
        for line in content:
            if int(line.strip("\n")) != biglietto.numero:
                f.write(line)

 
def insert(biglietto:Biglietto):
    f = open(path, "a")
    f.write(biglietto.__repr__())
    f.close() 
