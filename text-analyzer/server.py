from flask import Flask, render_template, request

app = Flask(__name__)

# Single route to handle multiple HTTP requests.
@app.route('/', methods=["GET", "POST"])
def index():
	data = ""
	if len(request.form) > 0:
		data = request.form["text"]
	return render_template("index.html", data=data)

app.run(host='0.0.0.0', port=81)