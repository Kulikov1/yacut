from datetime import datetime

from yacut import db
from .constants import DICT_FOR_URL, MAIN_URL


class URLMap(db.Model):
    """Модель URL."""

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(200), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=MAIN_URL + self.short,
        )

    def from_dict(self, data):
        for field in ['url', 'custom_id']:
            if field in data:
                setattr(self, DICT_FOR_URL[field], data[field])
