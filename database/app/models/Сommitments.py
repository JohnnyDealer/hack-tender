from datetime import datetime

from database.app import db


class Commitment(db.Model):
    __tablename__ = 'commitments'

    commitment_id = db.Column(db.Integer, primary_key=True)

    "Требуется обеспечение исполнения контракта"
    flag = db.Column(db.Boolean, default=True, nullable=True)

    "Размер обеспечения исполнения контракта"
    amount = db.Column(db.String, default='', nullable=True)

    "Порядок предоставления обеспечения гарантийных обязательств, требования к обеспечению"
    garanty = db.Column(db.String, default='', nullable=True)

    "Платежные реквизиты для обеспечения гарантийных обязательства"
    requisites = db.Column(db.String, default='', nullable=True)

    "Платежные реквизиты для обеспечения исполнения контракта"
    contract_requisites = db.Column(db.String, default='', nullable=True)

    purchases = db.relationship('Purchase', backref='order', lazy='dynamic')

    fields = {
        'amount': "Размер обеспечения исполнения контракта",
        'garanty': "Порядок предоставления обеспечения гарантийных обязательств, требования к обеспечению",
        'requisites': "Платежные реквизиты для обеспечения гарантийных обязательства",
        'contract_requisites': "Платежные реквизиты для обеспечения исполнения контракта"
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
