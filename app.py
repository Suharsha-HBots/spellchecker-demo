from flask import Flask, render_template, request, redirect,abort,flash
from spellchecker import SpellChecker
import re
import random

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    misspelled = []
    result = ""
    candidates = []
    txt = ""
    correct = ""
    spell = SpellChecker()
    # spell.word_frequency.load_text_file('./dict.txt')

    if request.method == "POST":
        txt = request.form.get("data")
        print(txt)
        if txt is not None:
            txt = re.sub("[^\w\s]", "", txt)
            words = txt.split()
            misspelled = spell.unknown(words)

            for word in words:
                if spell.unknown([word]):
                    correct = spell.correction(word)
                    candidates = spell.candidates(word)
                else:
                    correct = word
                result = result + " " + correct
                print(result)
    return render_template('index.html',a=result , correct = correct, misspelled=misspelled,list1=result,list2=candidates,len=len(misspelled))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)