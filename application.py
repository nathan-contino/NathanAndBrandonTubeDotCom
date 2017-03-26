from flask import Flask
from flask import render_template, request

application = Flask(__name__)
userList = open("username.txt").readlines()
#data = open("json/videos.json").read();

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
		infos = user.rstrip('\n').split(" ")
		print(infos)
		if (infos[0] == uname):
			if (infos[1] == pword):
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

	return render_template("thanku")

@application.route('/thanku')
def thanku():
	return render_template("thanku.html");

@application.route('/register')
def register():
	return render_template("register.html")

if __name__ == "__main__":
	application.debug = True
	application.run(port = 8080)