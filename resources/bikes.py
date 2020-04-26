import models


from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

bikes = Blueprint('bikes', 'bikes')

@bikes.route('/', methods=["GET"])
def bikes_index():
	result = models.Bike.select().dicts()
	return jsonify([bike for bike in result])

@bikes.route('/', methods=['POST'])
def create_bike():
	payload = request.get_json()
	print(payload)
	new_bike = models.Bike.create(brand=payload['brand'], model=payload['model'], biketype=payload['biketype'], gears=payload['gears'], brakes=payload['brakes'])
	print(new_bike)
	print(new_bike.__dict__)
	print(dir(new_bike))

	bike_dict = model_to_dict(new_bike)

	return jsonify(
		data=bike_dict,
		message="succesfully created bike",
		status=201
		), 201