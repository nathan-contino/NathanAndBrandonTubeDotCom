from flask import Flask
from flask import render_template, request, make_response, redirect
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
	return uList

def write_info():
	open('username.txt', 'a').close()
	f = open('username.txt', 'w')
	buffer = ''	
	for user in userList:
		buffer += user + ' '
		buffer += userList[user] + ' ' + '\n'
	f.write(buffer)
	f.close()

def read_info_message():
	f = open('messages.txt', 'r')
	filedata = f.read().split('\n')
	f.close()
	mList = {}
	for line in filedata:
		if line != '':
			val = line.split()
			mList[val[0]] = ' '.join(word for word in val[1:])
	return mList

def write_info_message():
	open('messages.txt', 'a').close()
	f = open('messages.txt', 'w')
	buffer = ''
	for mess in messageList:
		buffer += mess + ' '
		buffer += messageList[mess] + '\n'
	f.write(buffer)
	f.close()

application = Flask(__name__)
userList = read_info()
messageList = read_info_message()

@application.route('/')
def index():
	if 'username' in request.cookies:
		return redirect('/dynamichome')
	else:
		return render_template("index.html")

@application.route('/logout')
def logout():
	resp = make_response(render_template("thanku.html"))
	resp.set_cookie('username', expires=0)
	return resp

@application.route('/login', methods = ['GET'])
def login():
	uname = request.args.get('username')
	pword = request.args.get('password')
	print(userList)
	if (userList.get(uname)):
		if (userList.get(uname) == pword):
			redirect_to_thanks = redirect('/dynamichome')
			response = application.make_response(redirect_to_thanks)  
			response.set_cookie('username',value=uname)
			return response
		else: return "failure"

	return "no such user"

@application.route('/dynamichome')
def dynamicHome():
	if 'username' in request.cookies:
		return "Please go to your homepage <a href='/homepage?username={}'>here</a> <br/> Or check out some cool videos here <a href='/videos'>here</a> <br/><br/> Or if you want to logout click here: <a href='/logout'>this link</a>".format(request.cookies['username'])

@application.route('/sendmessage', methods = ['GET'])
def send():
	uname = request.args.get('username')
	mess = request.args.get('message')
	messageList[uname] = mess
	write_info_message()
	return render_template("thanks2.html")

@application.route('/homepage', methods = ['GET'])
def homepage():
	uname = request.args.get('username')
	return render_template("homepage.html", username = uname, message = messageList.get(uname))

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

	redirect_to_thanks = render_template("thanku.html")
	response = application.make_response(redirect_to_thanks)  
	response.set_cookie('username',value=uname)
	return response

@application.route('/videos')
def videos():
	return render_template("videos.html")

@application.route('/register')
def register():
	return render_template("register.html")

@application.route('/satellite')
def satellite():
	return render_template("satellite.html")

@application.route('/drone')
def drone():
	return render_template("drone.html")

@application.route('/montreal')
def montreal():
	return render_template("montreal.html")

@application.route('/hackertype')
def hackertype():
	return render_template("hackertype.html")

@application.route('/macbook')
def macbook():
	return render_template("macbook.html")

if __name__ == "__main__":
	application.debug = True
	application.run(port = 8080)