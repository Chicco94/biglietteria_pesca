from app.models import Biglietto, select_all, insert

TOT_BIGLIETTI = 2000

if __name__=="__main__":
    for numero in range(1,TOT_BIGLIETTI+1):
        insert(Biglietto(numero))

    print(select_all())
