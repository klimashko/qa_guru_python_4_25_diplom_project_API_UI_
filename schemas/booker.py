from voluptuous import Schema, PREVENT_EXTRA, All, Length




auth_create_token = Schema(
    {
        "token": str
    },
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