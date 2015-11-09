from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
	return '<h1>Hello world</h1>'


@app.route('/user/<name>')
def name(name):
	return 'Hello %s ' % name	



if __name__ == '__main__':
	app.run(debug = True)
	