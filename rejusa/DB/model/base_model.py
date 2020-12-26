from ..db_connector import DBConnector


class BaseModel(DBConnector):
    """
    Model básico, com inicialização de DBConnector
    """

    def __init__(self):
        self.metadata.create_all(DBConnector.get_engine())
        super().__init__()

    def to_dict(self) -> dict:
        """
        Conversão para dict. Necessário para transformar em json
        """
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data
