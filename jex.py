from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/login')

def login():
	return render_template("login.html")

if __name__ == '__main__':
	host = "127.0.0.1"
	port = 1337
	application.debug = True
	application.run(host, port)