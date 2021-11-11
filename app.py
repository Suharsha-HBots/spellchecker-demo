from flask import Flask, render_template, request, redirect,abort,flash
from spellchecker import SpellChecker
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    misspelled = []
    list1 = []
    candidates = []
    txt = ""
    correct = ""
    spell = SpellChecker()
    spell.word_frequency.load_text_file('./dict.txt')

    if request.method == "POST":
        txt = request.form.get('val')
        txt = re.sub("[^\w\s]", "", txt)
        words = txt.split()
        misspelled = spell.unknown(words)

        for word in misspelled:
            correct = correct + spell.correction(word)
            list1.append(spell.correction(word))
            candidates.append(spell.candidates(word))

    return render_template('index.html',a=txt , correct = correct, misspelled=misspelled,list1=list1,list2=candidates,len=len(misspelled) ,len1=len(list1))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)