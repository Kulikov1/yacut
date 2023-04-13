from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class URLMapForm(FlaskForm):
    """Форма для получения короткой ссылки."""
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 200)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(0, 16)]
    )
    submit = SubmitField('Создать')
