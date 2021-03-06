# Call models.py directly to initialize tables

from datetime import datetime

from app import db
from sqlalchemy.schema import UniqueConstraint


class FeatureRequest(db.Model):
    '''
    Model class for FeatureRequest. Contains fields and methods for class.
    '''
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    client = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    priority = db.Column(db.Integer)
    productarea = db.Column(db.String(100))

    constraint = db.UniqueConstraint('client', 'priority', name='clientpriority')

    def __init__(self, name, description, client, date, priority, productarea):
        self.name = name
        self.description = description
        self.client = client
        self.date = datetime.strptime(date, "%Y-%m-%d")
        if self.date.date() < datetime.now().date():
            raise Exception('Date cannot be in the past')
        self.priority = priority
        self.productarea = productarea
        self.__table_args__ = (self.constraint)


if __name__ == "__main__":
    print("Creating database tables")
    db.create_all()
    print("Done!")
