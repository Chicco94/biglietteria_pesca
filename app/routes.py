import random
from app import app
from app.forms import PreEstrazioneForm,PostEstrazioneForm
from flask import render_template, flash, redirect, url_for

BIGLIETTI = [i for i in range(10)]
def estrai():
    global BIGLIETTI
    random.shuffle(BIGLIETTI)
    return BIGLIETTI.pop()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/pre_estrazione', methods=['GET', 'POST'])
def pre_estrazione():
    form = PreEstrazioneForm()
    if form.validate_on_submit():
        return redirect(url_for('post_estrazione'))
    return render_template('pre_estrazione.html', form=form)


@app.route('/post_estrazione')
def post_estrazione():
    form = PostEstrazioneForm()
    if form.validate_on_submit():
        return redirect(url_for('pre_estrazione'))
    return render_template('post_estrazione.html', numero = estrai(), form = form)