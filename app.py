from flask import Flask, jsonify

from resources.bikes import bikes
from resources.users import users
import models
from flask_cors import CORS
from flask_login import LoginManager
DEBUG=True
PORT=8000
app =Flask(__name__) #ask if  this has to be name ?

app.secret_key="this is a secret shhhhh"
login_manager = LoginManager()

login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
	try:
		user = models.User.get_by_id(user_id)
		return user
	except models.DoesNoExist:
		return None

CORS(bikes, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(bikes, url_prefix='/api/v1/bikes/')
app.register_blueprint(users, url_prefix='/api/v1/users')
@app.route('/')
def hi():
	return 'hiiii'



if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)