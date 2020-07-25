from app import path

class Biglietto():
    
    def __init__(self, numero):
        self.numero = numero

    def __repr__(self):
        return '{}\n'.format(self.numero) 

def select_all():
    with open(path) as f:
        content = f.readlines() 
    return [Biglietto(int(x.strip())) for x in content if c.strip() != ""]

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
