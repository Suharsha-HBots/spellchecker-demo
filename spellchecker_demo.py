from spellchecker import SpellChecker
import re

spell = SpellChecker()
spell.word_frequency.load_dictionary('./dict.json')

txt = "Something is hapenning here"

# find those words that may be misspelled
txt = re.sub("[^\w\s]", "", txt)
print(txt)
words = txt.split()
print(words)
misspelled = spell.unknown(words)
print(misspelled)

for word in misspelled:
	print(word)
	# Get the one `most likely` answer
	print(spell.correction(word))

	# Get a list of `likely` options
	print(spell.candidates(word))
