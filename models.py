from peewee import *

DATABASE = SqliteDatabase('bikes.sqlite')

class Bike(Model):
	brand=CharField()
	model=CharField()
	bikeType=CharField()
	gears=SmallIntegerField()
	brakes=BooleanField()

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Bike], safe=True)
	print("connected to db and created tables")

	DATABASE.close()