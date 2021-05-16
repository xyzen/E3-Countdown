import datetime
from time import sleep
from flask import Flask, render_template, Response

def get_delta():
	delta = datetime.datetime(2021, 6, 12, 14) - datetime.datetime.today()
	delta = datetime.timedelta(days=delta.days, seconds=delta.seconds)
	if delta < datetime.timedelta(0):
		delta = datetime.timedelta(0)
	return str(delta).upper()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", delta=get_delta())

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=False, threaded=True)