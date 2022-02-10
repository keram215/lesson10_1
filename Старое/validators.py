def check_pin(pin):
    if len(pin) != 4:
        return False

    if pin == '1234':
        return False

    if len(set(pin)) ==1:
        return False

    for char in list(pin):
        if pin.count(char) == 4:
            return False

    return True


def check_pass(password):

    if len(password) < 8:
        return False

    if any(char.isdigit() for char in password):
        return False

    if any(char.isalpha() for char in password):
        return False

    return True


def check_mail(email):
    return '@' in email and '.' in email


def check_name(name):
    start_alpha_index= ord('А')
    end_alpha_index = ord('я')

    for char in name:
        if char == ' ':
            continue

        if char in ('Ё','ё'):
            continue

        if ord(char) < start_alpha_index or ord(char) > end_alpha_index:
            return False

    return True

#print(check_pin('1239'))
#print(check_pin('234'))
#print(check_pin('1111'))
#print(check_pin('0001'))
#rint(check_pin('aaaa'))

print(check_pass('aaadr'))
print(check_pass('dertaa'))
print(check_pass('dgfjhgkk;j;lh'))
print(check_pass('dgfjhgkk;j;lh'))

