from datetime import datetime
from sqlalchemy.orm import backref
from database.app import db


class Contract(db.Model):
    __tablename__ = 'contracts'

    contract_id = db.Column(db.Integer, primary_key=True)
    FZ = db.Column(db.String, nullable=False)
    win_date = db.Column(db.Date, default=datetime.utcnow, nullable=True)
    notice_number = db.Column(db.Integer, default=0, nullable=True)
    contract_term = db.Column(db.String(32), default='128', nullable=True)
    link = db.Column(db.String, nullable=True)
    protocol_date = db.Column(db.Date, default=datetime.utcnow, nullable=True)
    contract_finish_term = db.Column(db.String(32), default='128', nullable=True)
    prepay_amount = db.Column(db.Integer, default=0, nulable=True)

