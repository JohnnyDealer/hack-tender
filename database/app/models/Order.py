from datetime import datetime

from database.app import db


class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)

    "Уникальный номер плана-графика закупок"
    unique_number = db.Column(db.String, default='', nullable=True)

    "Финансовый год планирования"
    plan_year = db.Column(db.Integer, default=2020, nullable=True)

    "Плановый период"
    plan_period = db.Column(db.String, default='', nullable=True)

    "Дата утверждения плана-графика закупок"
    secure_date = db.Column(db.Date, default=datetime.utcnow(), nullable=True)

    "Дата размещения плана-графика закупок"
    start_date = db.Column(db.Date, default=datetime.utcnow(), nullable=True)

    "Статус"
    status = db.Column(db.String, default='', nullable=True)

    "Заказчик"
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), default=None,  nullable=True)

    fields = {
        'unique_number': "Уникальный номер плана-графика закупок",
        'plan_year': "Финансовый год планирования",
        'plan_period':  "Плановый период",
        'secure_date': "Дата утверждения плана-графика закупок",
        'start_date': "Дата размещения плана-графика закупок",
        'status': "Статус"
    }

    def from_dict(self, data):
        # Проверка на тип 'словарь'
        if type(data) != dict:
            raise Exception('no dictionary provided')

        for field in self.fields:
            if self.fields[field] in data:
                setattr(self, field, data[self.fields[field]])

    def __repr__(self):
        return "<Order № {}>".format(self.order_id)





    """order_id = db.Column(db.Integer, primary_key=True)
    FZ = db.Column(db.String, nullable=False)
    trading_volume = db.Column(db.Float, default=0.0, nullable=True)
    trading_amount = db.Column(db.Integer, default=0, nulable=True)
    registry_number = db.Column(db.Integer, default=0, nulable=True)
    purchase_subject = db.Column(db.String, default='', nulable=True)
    contract_sum = db.Column(db.Float, default=0.0, nullable=True)
    participation_amount = db.Column(db.Float, default=0.0, nullable=True)
    contractors_amount = db.Column(db.Float, default=0.0, nullable=True)
    placement_date = db.Column(db.Date, default=datetime.utcnow, nullable=True)
    application_deadline = db.Column(db.Date, default=datetime.utcnow, nullable=True)
    contract_start = db.Column(db.Date, default=datetime.utcnow, nullable=True)
    contract_end = db.Column(db.Date, default=datetime.utcnow, nullable=True)
    electronic_platform = db.Column(db.String, default='', nulable=True)
    purchase_period = db.Column(db.String, default='', nulable=True)
    trading_subject = db.Column(db.String, default='', nulable=True)

    notice_number = db.Column(db.Integer, default=0, nullable=True)
    contract_term = db.Column(db.String(32), default='128', nullable=True)
    link = db.Column(db.String, nullable=True)
    protocol_date = db.Column(db.Date, default=datetime.utcnow, nullable=True)
    contract_finish_term = db.Column(db.String(32), default='128', nullable=True)
    prepay_amount = db.Column(db.Integer, default=0, nulable=True)"""
