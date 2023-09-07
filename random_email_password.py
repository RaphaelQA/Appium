import random
import string
random_mail = ["gmail", "yandex", "mail"]
random_domen = [".ru", ".com"]


def random_email():
    first_part = ""
    for _ in range(8):
        first_part += random.choice(string.ascii_letters + string.digits)
    second_part = random.choice(random_mail)
    third_part = random.choice(random_domen)
    return f'{first_part}@{second_part}{third_part}'
def random_password():
    random_pass = ""
    for _ in range(8):
        random_pass += random.choice(string.ascii_letters + string.digits)
    return random_pass
def record_male(mail):
    with open('../delete_mail.txt', 'a') as f:
        f.write(f'{mail}\n')
