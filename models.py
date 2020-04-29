from peewee import *
from flask_login import UserMixin
DATABASE = SqliteDatabase('bikes.sqlite')


class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()

	class Meta:
		database = DATABASE

class Bike(Model):
	brand=CharField()
	model=CharField()
	biketype=CharField()
	gears=SmallIntegerField()
	brakes=BooleanField()
	owner=ForeignKeyField(User, backref='bikes')

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Bike], safe=True)
	print("connected to db and created tables")

	DATABASE.close()