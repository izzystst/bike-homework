from flask import Flask, jsonify

from resources.bikes import bikes

import models

DEBUG=True
PORT=8000
app =Flask(__name__) #ask if  this has to be name ?

app.register_blueprint(bikes, url_prefix='/api/v1/bikes')

@app.route('/')
def hi():
	return 'hiiii'


if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)