import re
from http import HTTPStatus

from flask import request

from . import app, db
from .constants import PATTERN_SHORT, LEN_USER_SHORT
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_custom_id():
    """Функция предоставляет короткий url на основании оригинального."""

    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' not in data or not(data['custom_id']):
        data['custom_id'] = get_unique_short_id()
    if not(re.match(PATTERN_SHORT, data['custom_id'])):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки',
            HTTPStatus.BAD_REQUEST
        )
    if len(data['custom_id']) > LEN_USER_SHORT:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    name = data['custom_id']
    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(f'Имя "{name}" уже занято.')
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return url.to_dict(), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_url(short_id):
    """Функция принимает короткое имя ссылки и отдает оригинальный url,
    если короткое имя есть в базе.
    """

    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return {'url': url.original}, HTTPStatus.OK
