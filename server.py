# coding: utf-8
"""
Belle Marquise generator

"
On les peut mettre premièrement comme vous avez dit :
"Belle Marquise, vos beaux yeux me font mourir d’amour".

Ou bien :
"D’amour mourir me font, belle Marquise, vos beaux yeux".

Ou bien :
"Vos yeux beaux d’amour me font, belle Marquise, mourir".

Ou bien :
"Mourir vos beaux yeux, belle Marquise, d’amour me font".

Ou bien :
"Me font vos yeux beaux mourir, belle Marquise, d’amour."

Le Bourgeois gentilhomme, II, 4

"""
from __future__ import print_function
from itertools import permutations
from random import choice
from flask import (
    render_template,
    Flask
)


phrases = []
app = Flask(__name__)


def generate_all_phrases():
    global phrases
    for beautiful_eyes in ["beaux yeux", "yeux beaux"]:

        words = [
            "belle Marquise",
            "vos {}".format(beautiful_eyes),
            "me font",
            "mourir",
            "d'amour"
        ]
        for perm in permutations(words, len(words)):
            phrase = ' '.join(perm)
            phrases.append('{}.'.format(phrase))

    phrases = map(lambda x: x[0].upper() + x[1:], phrases)


@app.route('/')
def root(name=None):
    return render_template('index.html', marquise=choice(phrases))


if __name__ == '__main__':
    generate_all_phrases()
    app.run(host='0.0.0.0', debug=True)
