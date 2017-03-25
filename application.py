from flask import Flask
from flask import render_template, request

application = Flask(__name__)

@application.route('/')
def index():
	return render_template("index.html")

if __name__ == "__main__":
    application.debug = True
    application.run(port = 8080)