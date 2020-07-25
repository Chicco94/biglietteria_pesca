import os
from flask import Flask, render_template
import random

BIGLIETTI = range(10)

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/estrai',methods=['POST'])
def estrai():
    global BIGLIETTI
    random.shuffle(BIGLIETTI)
    print(BIGLIETTI.pop())

if __name__ == '__main__':

    app.run()


