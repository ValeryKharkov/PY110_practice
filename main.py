from faker import Faker
fake_ru = Faker('ru_RU')

# fake_ru.phone_number(), fake_ru.job(), fake_ru.address()


def data():
    return fake_ru.name()


f = open('task.txt', 'w', encoding='utf8')

for i in range(10):
    f.write(data())