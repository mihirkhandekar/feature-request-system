from flask import render_template, request
from flask import jsonify, make_response
from flask_cors import CORS, cross_origin

from models import FeatureRequest, add_request
from app import app



@app.route('/api/featurerequest', methods=['GET', 'POST'])
@cross_origin()
def add():

    if request.method == 'GET':
        rqs = FeatureRequest.query.all()
        response = []
        for rq in rqs:
            response.append({'name': rq.name, 'description': rq.description, 'date': rq.date, 'priority': rq.priority, 'client': rq.client})
        return make_response(jsonify(response), 200)

    name = request.form.get('name')
    description = request.form.get('description')
    client = request.form.get('client')
    date = request.form.get('date')
    priority = request.form.get('priority')
    productarea = request.form.get('productarea')

    rq = add_request(name, description, client, date, priority, productarea)
    print('DONE')
    return '', 201
