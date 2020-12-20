from datetime import datetime

from database.app import db


class Purchase(db.Model):
    __tablename__ = 'purchases'

    purchase_id = db.Column(db.Integer, primary_key=True)

    "Начальная (максимальная) цена контракта"
    contract_amount = db.Column(db.String, default='', nullable=True)

    "Валюта"
    currency = db.Column(db.String, default='', nullable=True)

    "Источник финансирования"
    finance = db.Column(db.String, default='', nullable=True)

    "Сведения о связи с позицией плана-графика"
    plan_info = db.Column(db.String, default='', nullable=True)

    commitment_id = db.Column(db.Integer, db.ForeignKey('commitments.commitment_id'), default=0,  nullable=True)

    fields = {

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
