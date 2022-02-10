from validators import check_name, check_mail, check_pass, check_pin
USERS_DATA = [
    {
        'pin': '1239',
        'password' : 'secret100',
        'email': 'local@skypro',
        'name': 'Данил'

    },
    {
        'pin': '3333',
        'password' : '123456789',
        'email': 'me@sky.pro',
        'name': 'Р_и_т_а',
    },
    {
        'pin': '1232',
        'password' : 'qwerty12345',
        'email': 'examle@example.com',
        'name': 'Иван',
    }
]


for data in USERS_DATA:
    validation = all(
        [
            check_pin(data['pin']),
            check_pass(data['password']),
            check_mail(data['email']),
            check_name(data['name']),
        ]
    )
    print(data['pin'], validation)

