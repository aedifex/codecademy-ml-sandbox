from texts import text_counter, text_training
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, render_template, request
import os
import logging

def analyize_text(text):
	logging.basicConfig(level=logging.ERROR)
	LOG = logging.getLogger(__name__)

	# intercepted_text = "I love my job at Lacework!"
	# intercepted_text = input("Please enter text to be analyzed: ")
	intercepted_text = text

	text_counts = text_counter.transform([intercepted_text])

	text_classifier = MultinomialNB()

	text_labels = [0] * 1000 + [1] * 1000

	text_classifier.fit(text_training, text_labels)

	final_pos = text_classifier.predict_proba(text_counts)[0][1]

	final_neg = text_classifier.predict_proba(text_counts)[0][0]

	"""
	if final_pos > final_neg:
	  print("\nThe text sentiment is positive.\n")
	else:
	  print("\nThe text sentiment is negative.\n")
	"""

	if final_pos > final_neg:
		return "The sentiment is positive"
	else:
		return "The sentiment is negative"

# Server specific functionality
app = Flask(__name__)

# Single route to handle multiple HTTP requests.
@app.route('/', methods=["GET", "POST"])
def index():
	data = ""
	if len(request.form) > 0:
		# data = request.form["text"]
		data = analyize_text(request.form["text"])
	return render_template("index.html", data=data)

if __name__ == "__main__":
	# app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
