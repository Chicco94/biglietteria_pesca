from app import db

class Biglietto(db.Model):
    
    def __init__(self, numero):
        self.numero = numero

    def __repr__(self):
        return '{}'.format(self.numero) 

def select_all():
    content = db.readlines()
    return [x.strip() for x in content]

def insert(biglietto:Biglietto):
    db.write(biglietto.__repr__()) 
