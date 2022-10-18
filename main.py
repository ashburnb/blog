from flask import Flask, render_template

# create the Flask instance app
app = Flask(__name__)

# decorator route to home page
@app.route('/')
def index():
	title = 'Brad\'s Blog'
	return render_template('index.html', title=title)

# decorator route to user page
@app.route('/user/<name>')
def user(name):
	title = 'User Brad'
	return render_template('user.html', name=name, title=title)


# Invalid URL Error
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500



