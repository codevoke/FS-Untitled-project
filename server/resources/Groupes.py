from flask_restful import Resource
from models import GroupList as GroupListTable


class Groupes(Resource):
    path = "/groupes"

    @classmethod
    def get(cls):
        groupes = GroupListTable.get_all()

        if groupes:
            return [g.json() for g in groupes]
        else:
            return {"message": "No groupes found"}, 404