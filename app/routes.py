import random
from app import app
from app.forms import InputForm
from flask import render_template, flash, redirect, url_for

BIGLIETTI = [i for i in range(10)]
BIGLIETTO_ESTRATTO = -1
def estrai():
    global BIGLIETTI
    global BIGLIETTO_ESTRATTO
    random.shuffle(BIGLIETTI)
    return BIGLIETTI.pop()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/pre_estrazione', methods=['GET', 'POST'])
def pre_estrazione():
    form = InputForm()
    if form.validate_on_submit():
        return redirect(url_for('post_estrazione'))
    return render_template('pre_estrazione.html', form=form)


@app.route('/post_estrazione')
def post_estrazione():
    return render_template('post_estrazione.html', numero = estrai())