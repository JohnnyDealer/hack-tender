from datetime import datetime

from database.app import db


class Contract(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
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
    prepay_amount = db.Column(db.Integer, default=0, nulable=True)
