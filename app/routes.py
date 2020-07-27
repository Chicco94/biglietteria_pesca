import random
from app import app
from app.models import *
from app.forms import PreEstrazioneForm,PostEstrazioneForm
from flask import render_template, flash, redirect, url_for

ALREADY_DREW = False

def estrai():
    biglietti = select_all()
    random.shuffle(biglietti)
    biglietto = biglietti.pop()
    delete(biglietto)
    return biglietto


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/pre_estrazione', methods=['GET', 'POST'])
def pre_estrazione():
    global ALREADY_DREW
    form = PreEstrazioneForm()
    ALREADY_DREW = False
    if form.validate_on_submit():
        return redirect(url_for('post_estrazione'))
    return render_template('pre_estrazione.html', form=form)


@app.route('/post_estrazione', methods=['GET', 'POST'])
def post_estrazione():
    global ALREADY_DREW
    form = PostEstrazioneForm()
    if not ALREADY_DREW:
        BIGLIETTO = estrai()
        BIGLIETTO.printZebra()
        ALREADY_DREW = True
    if form.validate_on_submit():
        return redirect(url_for('pre_estrazione'))
    return render_template('post_estrazione.html', numero = BIGLIETTO, form = form)