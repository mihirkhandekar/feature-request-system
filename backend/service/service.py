import sys

import numpy as np
from models import FeatureRequest
from service.ml.similarity_checker import get_difference_score

from app import db

SIMILARITY_THRESHOLD = 0.7  # Configurable threshold to consider 2 sentences as simliar


def get_common_description_count(descriptions, description):
    '''
    Function to compare description with all descriptions and return number of descriptions with simlarity score higher than threshold
    '''
    count = 0
    print(descriptions)
    for db_description in descriptions:
        score = get_difference_score(db_description, description)
        if score > SIMILARITY_THRESHOLD:
            count += 1
    return count


def add_request(name, description, client, date, priority, productarea):
    '''
    Function to insert request into database.
    '''
    priority = int(priority)
    client_data = FeatureRequest.query.filter_by(client=client.lower()).all()
    all_data = FeatureRequest.query.all()
    client_priorities = [int(c.priority) for c in client_data]
    descriptions = [str(c.description) for c in all_data]

    sim_count = get_common_description_count(descriptions, description)

    # If priority is duplicated, priorities of other requests of same client are shifted ahead. Else, the priority is added to the last position
    if priority not in client_priorities:
        if len(client_priorities) == 0:
            priority = 1
        else:
            priority = max(client_priorities) + 1
        feat_request = FeatureRequest(
            name, description, client.lower(), date, priority, productarea)
        db.session.add(feat_request)
        db.session.commit()
    else:
        feat_request = FeatureRequest(
            name, description, client.lower(), date, priority, productarea)
        db.session.add(feat_request)
        for c in client_data:
            if c.priority >= priority:
                c.priority += 1
                db.session.add(c)
        db.session.commit()
    return sim_count


def get_all_requests():
    '''
    Function to fetch and return all feature requests
    '''
    rqs = FeatureRequest.query.all()
    response = []
    for rq in rqs:
        response.append({'name': rq.name, 'description': rq.description, 'date': rq.date,
                         'priority': rq.priority, 'client': rq.client, 'area': rq.productarea})
    return response
