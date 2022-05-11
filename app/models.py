from app import db
from datetime import datetime

class Beds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), index=True)
    ward_id = db.Column(db.Integer, db.ForeignKey('wards.id'))
    signals = db.relationship('Signals', backref='bed', lazy='dynamic')
    def __repr__(self):
        return '<Кровать {} Палата {} Отделение {}>'.format(self.name, self.ward.name, self.ward.branch.name)

class Wards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), index=True)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'))
    beds = db.relationship('Beds', backref='ward', lazy='dynamic')
    def __repr__(self):
        return '<Ward {}>'.format(self.name)

class Branches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), index=True)
    wards = db.relationship('Wards', backref='branch', lazy='dynamic')
    def __repr__(self):
        return '<Branch {}>'.format(self.name)

class Signals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime(), default=datetime.now)
    bed_id = db.Column(db.Integer, db.ForeignKey('beds.id'))
    status = db.Column(db.String())
