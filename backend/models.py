from app import db
from datetime import datetime

class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    client = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    priority = db.Column(db.Integer)
    productarea = db.Column(db.String(100))


    def __init__(self, name, description, client, date, priority, productarea):
        self.name = name
        self.description = description
        self.client = client
        self.date = datetime.strptime(date, "%Y-%m-%d")
        if self.date.date() < datetime.now().date():
            raise Exception('Date cannot be in the past')
        self.priority = priority
        self.productarea = productarea


if __name__ == "__main__":
    print("Creating database tables...")
    db.create_all()
    print("Done!")
