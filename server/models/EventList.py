from .db import db


class EventList(db.Model):
    __tablename__ = "EVENT_LIST"

    EL_ID = db.Column(db.Integer, primary_key=True)
    EL_NAME = db.Column(db.String(50), nullable=False)
    EL_START_DATE = db.Column(db.Timestamp)
    EL_END_DATE = db.Column(db.Timestamp)
    EL_GROUP_ID = db.Column(db.Integer, db.ForeignKey('GROUP_LIST.GL_ID'), nullable=False)
    EL_STUDENT_ID = db.Column(db.Integer, db.ForeignKey('STUDENT.S_ID'), nullable=False)
    EL_STAFF_ID = db.Column(db.Integer, db.ForeignKey('STAFF_LIST.SL_ID'), nullable=False)

    def json(self):
        return {
            "EL_ID": self.EL_ID,
            "EL_NAME": self.EL_NAME,
            "EL_START_DATE": self.EL_START_DATE,
            "EL_END_DATE": self.EL_END_DATE,
            "EL_GROUP_ID": self.EL_GROUP_ID,
            "EL_STUDENT_ID": self.EL_STUDENT_ID,
            "EL_STAFF_ID": self.EL_STAFF_ID
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
