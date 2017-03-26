from flask import Flask
from flask import render_template, request
import csv

application = Flask(__name__)
userList = csv.DictReader(open("username.txt", 'rw'), delimiter=' ')
# data = open("json/videos.json").read();

def write_data_to_file():
	file = open("username.txt");
	for u in userList:
		file.write(u, ' ', userList[u]);

@application.route('/')
def index():
	return render_template("index.html")

@application.route('/login', methods = ['GET'])
def login():
	uname = request.args.get('username')
	pword = request.args.get('password')

	for user in userList:
		if (user['username'] == uname):
			if (user['password'] == pword):
				return "success"
			else: return "failure"

	return "no such user"


@application.route('/makelogin', methods = ['GET'])
def makelogin():
	uname = request.args.get('username')
	pword = request.args.get('password')
	pwordconfirm = request.args.get('confirm')

	if pword == pwordconfirm:
		userList[uname] = pword;
	else: 
		return render_template("register")

	write_data_to_file()

	return render_template("login")

@application.route('/register')
def register():
	return render_template("register.html")

if __name__ == "__main__":
	application.debug = True
	application.run(port = 8080)