import string
import random

from flask import flash, redirect, render_template

from . import app, db
from .constants import LEN_RANDOM_SHORT, MAIN_URL
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    """Функция отдает строку длиной K, состоящую из
    больших и маленьких латинских букв и цифр в случайном порядке.
    """

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    return ''.join(random.choices(lower + upper + digits, k=LEN_RANDOM_SHORT))


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Вью-функция для основной страницы"""

    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form)
        if short is None or len(short) == 0:
            short = get_unique_short_id()
            while URLMap.query.filter_by(short=short).first():
                short = get_unique_short_id()
        urlmap = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(urlmap)
        db.session.commit()
        return render_template('index.html', form=form, short=MAIN_URL + short)
    return render_template('index.html', form=form)


@app.route('/<short>')
def redirect_view(short):
    """Вью-функция эндпоинта с именем короткой ссылки.
    Если короткое имя ссылки есть в базе, то функция редиректит
    пользователя на оригинальную ссылку
    """

    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)
