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

@bikes.route('/<id>', methods=['DELETE'])
def delete_bike(id):
	delete_query = models.Bike.delete().where(models.Bike.id==id)
	num_rows_deleted = delete_query.execute()
	print(num_rows_deleted)
	return jsonify(
		data={},
		message="deleted bike {} with id {}".format(num_rows_deleted, id),
		status=200
		), 200