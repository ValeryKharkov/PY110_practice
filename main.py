import json

from faker import Faker

fake_ru = Faker('ru_RU')

dict_ = {}
for i in range(250):
    name = fake_ru.name()
    phone = fake_ru.phone_number()
    job = fake_ru.job()
    address = fake_ru.address()
    dict_[i] = {name: [address, job, phone]}
    with open('DS.txt', 'w', encoding='utf8') as f:
        json.dump(dict_, f, indent=4, ensure_ascii=False)
