from app.app_data import db


class DeviceData(db.Model):
    __tablename__ = "device_data"

    id = db.Column(db.BigInteger, primary_key=True)
    device_id = db.Column(db.BigInteger)
    type = db.Column(db.Text)
    value = db.Column(db.Float)
    created_at = db.Column(db.DateTime)

    def get_id(self):
        return self.id

    def to_dict(self, scenario):
        if not scenario:
            return {}

        keys = []

        if scenario == "out":
            keys = ["value", "created_at"]

        return dict([(k, getattr(self, k)) for k in keys])
