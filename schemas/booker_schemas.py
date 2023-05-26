from voluptuous import Schema, PREVENT_EXTRA, All, Length


def is_email_true(email): #Это для примера, простая ф-ия, лучше с помощью регулярки сделать
    if '@' in email and '.' in email:
        return True
    else:
        raise ValueError('Это не емэйл')

user_schema = Schema(
    {
        "id": int,
        "email": All(str, is_email_true), #Этот валидатор сравнивает значение "email" в функции is_email_true(email)
        "first_name": str,
        "last_name": str,
        "avatar": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)

list_users_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": All([user_schema], Length(min=1)),  #Этот валидатор устанавливает длину списка [user_schema], min=1
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

single_user_schema = Schema(
    {"data": {
        "id": int,
        "email": All(str, is_email_true),  #Этот валидатор сравнивает значение "email" в функции is_email_true(email)
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
        "support": {
            "url": str,
            "text": str
        }},
    extra=PREVENT_EXTRA,
    required=True
)

login_schema = Schema(
    {
        'token': str
    },
    extra=PREVENT_EXTRA,
    required=True
)

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

register_unsuccessfull_schema = Schema(
    {
        "error": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_user_schema = Schema(
    {
        'name': str,
        'job': str,
        'updatedAt': str
    },
    extra=PREVENT_EXTRA,
    required=True
)

register_user_schema = Schema(
    {
        "id": int,
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

unsuccessfull_login_schema = Schema(
    {
        "error": str
    },
    extra=PREVENT_EXTRA,
    required=True
)