from flask import Flask
from flask import render_template, request

application = Flask(__name__)

@application.route('/')
def index():
	return "bonjour monde"

if __name__ == "__main__":
    application.debug = True
    application.run(port = 8080)