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
from itertools import permutations
from random import choice
from flask import (
    render_template,
    Flask
)


phrases = []
app = Flask(__name__)


def generate_all():
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
            perm = list(perm)
            belle_marquise_index = perm.index(words[0])
            # belle Marquise does not start the sentence
            if belle_marquise_index != 0:
                perm[belle_marquise_index - 1] = perm[belle_marquise_index - 1] + ','

            if belle_marquise_index != len(words) - 1:
                perm[belle_marquise_index] = perm[belle_marquise_index] + ','

            phrase = ' '.join(perm)
            phrases.append(phrase + '.')
    # uppercase the 1st
    phrases = list(map(lambda p: p[0].upper() + p[1:], phrases))


@app.route('/')
def root(name=None):
    return render_template('index.html', marquise=choice(phrases))


if __name__ == '__main__':
    generate_all()
    app.run(host='0.0.0.0', debug=True)
