from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent') 
	print request.headers
	return '<p>Your browser is %s</p>' % user_agent	

@app.route('/bad')
def bad():
	user_agent = request.headers.get('User-Agent') 
	print request.headers
	return '<p>Bad REquest', 400

@app.route('/redirect')
def redirect_func():
	return redirect('http://www.google.com')	


if __name__ == '__main__':
	app.run(debug = True)	