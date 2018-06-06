"""tools.

- name
- email
- phone
- company_name

"""
import json

from faker import Faker


def generate_name(number):
    faker = Faker('zh_CN')
    for _ in range(number):
        yield faker.name()


def generate_email(number, domain=None):
    faker = Faker('zh_CN')
    for _ in range(number):
        yield faker.email(domain=domain)


def generate_phone(number):
    faker = Faker('zh_CN')
    for _ in range(number):
        yield faker.phone_number()


def generate_company(number):
    faker = Faker('zh_CN')
    for _ in range(number):
        yield faker.company()


SUPPORTS = {
    'company': 'company',
    'phone': 'phone_number',
    'name': 'name',
    'email': 'email'
}


def generate_list(fields, number):
    faker = Faker('zh_CN')
    dataset = []
    for _ in range(number):
        item = {}
        for field in fields:
            func = getattr(faker, SUPPORTS.get(field))
            item[field] = func()
        dataset.append(item)

    return dataset


def export_json(data, ensure_ascii=False, indent=2):
    result = json.dumps(data, ensure_ascii=ensure_ascii, indent=indent)

    return result
