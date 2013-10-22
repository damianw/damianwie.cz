import os
from flask import Flask, render_template, send_from_directory, abort, redirect, url_for
import pyjade

app = Flask(__name__)
# use the jade template engine
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# redirect users to damianwie.cz/orek
@app.route('/')
def index():
	return redirect(url_for('orek'))

# my full name :)
@app.route('/orek')
def orek():
	obj = {
		"title": "Damian Wieczorek",
		"text": "A temporary homepage..."
	};
	return render_template('orek.jade', **obj)

# this guy handles static files
@app.route('/<path:filename>')
def send_pic(filename):
	print(filename)
	return send_from_directory('./public/', filename)

if __name__ == '__main__':
	# Bind to PORT if defined (on production)
	port = int(os.environ.get('PORT', 3000))
	
	app.run(host='0.0.0.0', port=port, debug=True)


