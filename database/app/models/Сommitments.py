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
        'ERUS_number': "Номер реестровой записи в ЕРУЗ",
        'status': "Статус регистрации",
        'provider_type':  "Тип участника закупки",
        'registration_start': "Дата регистрации в ЕИС",
        'registration_end': "Дата окончания срока регистрации в ЕИС",
        'full_name':  "Полное наименование",
        'address': "Адрес в пределах места нахождения",
        'OKVED': "Код(ы) ОКВЭД",
        'phone': "Контактный телефон",
        'INN': "ИНН",
        'KPP': "КПП",
        'tax_registration': "Дата постановки на учет в налоговом органе",
        'OGRN': "ОГРН",
        'email': "Адрес электронной почты",
        'mail': "Почтовый адрес",
        'FIO': "ФИО",
        'OGRNIP': "ОГРНИП",
        'ip_registration_date': "Дата регистрации индивидуального предпринимателя",
        'small_business': "Участник закупки является субъектом малого предпринимательства"
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
