from datetime import datetime

from database.app import db


class Provider(db.Model):
    __tablename__ = 'providers'

    provider_id = db.Column(db.Integer, primary_key=True)

    "Номер реестровой записи в ЕРУЗ"
    ERUS_number = db.Column(db.String, default='', nullable=True)

    "Статус регистрации"
    status = db.Column(db.String, default='', nullable=True)

    "Тип участника закупки"
    provider_type = db.Column(db.String, default='', nullable=True)

    "Дата регистрации в ЕИС"
    registration_start = db.Column(db.Date, default=datetime.utcnow(), nullable=True)

    "Дата окончания срока регистрации в ЕИС"
    registration_end = db.Column(db.String, default='', nullable=True)

    "Полное наименование"
    full_name = db.Column(db.String, nullable=True)

    "Сокращенное наименование"
    name = db.Column(db.String, nullable=True)

    "Адрес в пределах места нахождения"
    address = db.Column(db.String, default='', nullable=True)

    "Код(ы) ОКВЭД"
    OKVED = db.Column(db.String, default='', nullable=True)

    "Контактный телефон"
    phone = db.Column(db.String, default='', nullable=True)

    "ИНН"
    INN = db.Column(db.String, default='', nullable=True)

    "КПП"
    KPP = db.Column(db.String, default='', nullable=True)

    "Дата постановки на учет в налоговом органе"
    tax_registration = db.Column(db.Date, default=datetime.utcnow(), nullable=True)

    "ОГРН"
    OGRN = db.Column(db.String, default='', nullable=True)

    "Адрес электронной почты"
    email = db.Column(db.String, default='', nullable=True)

    "Почтовый адрес"
    mail = db.Column(db.String, default='', nullable=True)

    "ФИО"
    FIO = db.Column(db.String, default='', nullable=True)

    "ОГРНИП"
    OGRNIP = db.Column(db.String, default='', nullable=True)

    "Дата регистрации индивидуального предпринимателя"
    ip_registration_date = db.Column(db.String, default='', nullable=True)

    "Участник закупки является субъектом малого предпринимательства"
    small_business = db.Column(db.String, default='', nullable=True)

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
