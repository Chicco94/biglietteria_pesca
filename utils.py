from app.models import Biglietto, select_all, insert, date

TOT_BIGLIETTI = 2000

if __name__=="__main__":
    today = date.today()
    for numero in range(1,TOT_BIGLIETTI+1):
        insert(Biglietto(numero, today))

    print(select_all())
