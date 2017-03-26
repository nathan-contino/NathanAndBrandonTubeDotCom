from flask import Flask
from flask import render_template, request
import csv

def read_info():
	f = open('username.txt', 'r')
	filedata = f.read().split('\n')
	f.close()
	uList = {}
	for line in filedata:
		if line != '':
			val = line.split()
			uList[val[0]] = val[1]
	return uList;

application = Flask(__name__)
userList = read_info();

def write_info():
	open('username.txt', 'a').close()
	f = open('username.txt', 'w')
	buffer = ''	
	for user in userList:
		buffer += user + ' '
		buffer += userList[user] + ' '
	f.write(buffer)
	f.close()

@application.route('/')
def index():
	return render_template("index.html")

@application.route('/login', methods = ['GET'])
def login():
	uname = request.args.get('username')
	pword = request.args.get('password')
	print(userList)
	if userList[uname]:
		if (userList[uname] == pword):
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

	write_info()

	return render_template("thanku.html")

@application.route('/register')
def register():
	return render_template("register.html")

@application.route('/satellite')
def satellite():
	return render_template("satellite.html")

if __name__ == "__main__":
	application.debug = True
	application.run(port = 8080)