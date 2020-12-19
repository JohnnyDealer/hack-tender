from database.app.models import Provider
from database.app import db


class ProviderBuilder:

    @staticmethod
    def build(dictionary_list):
        """
        Добавляет в БД новых providers
        :param  dictionary_list: словарь словарей (или список)
        :return: void
        """
        for data in dictionary_list:
            provider = Provider()
            provider.from_dict(data)
            db.session.add(provider)
            db.session.commit()
