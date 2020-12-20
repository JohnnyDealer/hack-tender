from datetime import datetime
from sqlalchemy.orm import backref
from database.app import db


class Customer(db.Model):
    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key=True)

    "Наименование Заказчика"
    name = db.Column(db.String, default='', nullable=True)

    "ИНН"
    INN = db.Column(db.String, default='', nullable=True)

    "КПП"
    KPP = db.Column(db.String, default='', nullable=True)

    "ОКОПФ"
    OKOPF = db.Column(db.String, default='', nullable=True)

    "ОКТМО"
    OKTMO = db.Column(db.String, default='', nullable=True)

    "Публично-правовое образование"
    place = db.Column(db.String, default='', nullable=True)

    person_id = db.Column(db.Integer, db.ForeignKey('persons.person_id'), default=None,  nullable=True)

    orders = db.relationship('Order', backref='customer', lazy='dynamic')

    fields = {
        'name': "Наименование Заказчика",
        'INN': "ИНН",
        'KPP': "КПП",
        'OKOPF': "ОКОПФ",
        'OKTMO': "ОКТМО",
        'place': "Публично-правовое образование",
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
