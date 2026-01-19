from database.dao import DAO

class Model:
    def __init__(self):
        pass

    def get_anno(self):
        return DAO.read_anno()

    def get_forma(self):
        return DAO.read_forma()
