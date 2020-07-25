from app import db
from app.models import Biglietto, select_all, insert

TOT_BIGLIETTI = 100

if __name__=="__main__":
    for numero in range(TOT_BIGLIETTI):
        insert(Biglietto(numero))

    print(select_all())
