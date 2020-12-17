from flask import render_template, request
from flask import jsonify, make_response
from flask_cors import CORS, cross_origin

from service.service import add_request, get_all_requests
from app import app


@app.route('/api/featurerequest', methods=['GET', 'POST'])
@cross_origin()
def add():
    if request.method == 'GET':
        response = get_all_requests()
        return make_response(jsonify(response), 200)

    name = request.form.get('name')
    description = request.form.get('description')
    client = request.form.get('client')
    date = request.form.get('date')
    priority = request.form.get('priority')
    productarea = request.form.get('productarea')

    try:
        sim_count = add_request(name, description, client,
                            date, priority, productarea)
        return jsonify({'message': 'Successfully added!', 'similarity_count': sim_count}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 400
    
