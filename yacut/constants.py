MAIN_URL = 'http://localhost/'
LEN_RANDOM_SHORT = 6
LEN_USER_SHORT = 16
#Проверяет, что в строке только латиница и цифры
PATTERN_SHORT = r'^[a-zA-Z0-9]+$'
#Валидация короткой ссылки в форме. Должна быть пустой строкой, либо
#состоять из латиницы и цифр
SHORT_FORM_VALID = r'^\s*$|[A-Za-z0-9]'
DICT_FOR_URL = {
    'url': 'original',
    'custom_id': 'short',
}