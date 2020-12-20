from datetime import datetime

from database.app import db


class Person(db.Model):
    __tablename__ = 'persons'

    person_id = db.Column(db.Integer, primary_key=True)

    "ФИО лица, утвердившего план-график закупок"
    FIO = db.Column(db.String, default='', nullable=True)

    "Телефон"
    phone = db.Column(db.String, default='', nullable=True)

    "Адрес электронной почты"
    email = db.Column(db.String, default='', nullable=True)

    "Место нахождения (адрес)"
    address = db.Column(db.String, default='', nullable=True)

    customers = db.relationship('Customer', backref='person', lazy='dynamic')

    fields = {
        'FIO': "ФИО лица, утвердившего план-график закупок",
        'phone': "Телефон",
        'email':  "Адрес электронной почты",
        'address': "Место нахождения (адрес)"
    }

    def from_dict(self, data):
        # Проверка на тип 'словарь'
        if type(data) != dict:
            raise Exception('no dictionaries provided')

        for field in self.fields:
            if self.fields[field] in data:
                setattr(self, field, data[self.fields[field]])

    def __repr__(self):
        return "<Provider № {}>".format(self.provider_id)
