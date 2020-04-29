import models


from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required
bikes = Blueprint('bikes', 'bikes')

@bikes.route('/', methods=["GET"])
def bikes_index():
	current_user_bike_dicts = [model_to_dict(bike) for bike in current_user.bikes]

	for bike_dict in current_user_bike_dicts:
		bike_dict['owner'].pop('password')
	
	print(current_user_bike_dicts)

	return jsonify({
		'data': current_user_bike_dicts,
		'message':f"succesfuly found {len(current_user_bike_dicts)} bikes",
		'status': 200
		}), 200

@bikes.route('/', methods=['POST'])
def create_bike():
	payload = request.get_json()
	print(payload)
	new_bike = models.Bike.create(brand=payload['brand'], model=payload['model'], biketype=payload['biketype'], gears=payload['gears'], brakes=payload['brakes'], owner=current_user.id)
	print(new_bike)
	print(new_bike.__dict__)
	print(dir(new_bike))

	bike_dict = model_to_dict(new_bike)
	bike_dict['owner'].pop('password')

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

@bikes.route('<id>', methods=["PUT"])
def update_bike(id):
	payload = request.get_json()
	update_query = models.Bike.update(
		brand=payload['brand'], 
		model=payload['model'],
		biketype=payload['biketype'], 
		gears=payload['gears'], 
		brakes=payload['brakes']).where(models.Bike.id==id)
	num_rows_modified = update_query.execute()
	updated_bike = models.Bike.get_by_id(id)
	update_bike_dict = model_to_dict(updated_bike)

	return jsonify(
		data=update_bike_dict,
		message="updated dog with id {}".format(id),
		status=200
		), 200



