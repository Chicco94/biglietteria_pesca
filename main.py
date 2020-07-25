import os
from flask import Flask, render_template
import random

BIGLIETTI = [i for i in range(10)]

BIGLIETTO_ESTRATTO = "Prendi un biglietto"

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', variable=BIGLIETTO_ESTRATTO)

@app.route('/background_process_test')
def background_process_test():
    global BIGLIETTI
    global BIGLIETTO_ESTRATTO
    random.shuffle(BIGLIETTI)
    BIGLIETTO_ESTRATTO = BIGLIETTI.pop()
    print(BIGLIETTO_ESTRATTO)
    return 'OK'

if __name__ == '__main__':
    app.run()


