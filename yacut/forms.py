from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

from .constants import SHORT_FORM_VALID


class URLMapForm(FlaskForm):
    """Форма для получения короткой ссылки."""
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(max=1500)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(max=16),
                    Regexp(SHORT_FORM_VALID,
                    message='Ссылка должна состоять из латиницы и цифр')]
    )
    submit = SubmitField('Создать')
