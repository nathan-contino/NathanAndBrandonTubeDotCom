from flask import Flask
from flask import render_template, request

application = Flask(__name__)

@application.route('/')
def index():
	return render_template("index.html")

@application.route('/login', methods = ['GET'])
def login():

	userList = open("username.txt").readlines()
	uname = request.args.get('username')
	pword = request.args.get('password')

	for user in userList:
		infos = user.rstrip('\n').split(" ")
		print(infos)
		if (infos[0] == uname):
			if (infos[1] == pword):
				return "success"
			else: return "failure"

	return "no such user"

if __name__ == "__main__":
    application.debug = True
    application.run(port = 8080)