from faker import Faker


fake = Faker('ru_RU')

print(fake.first_name())
print(fake.last_name())
print(fake.email())
print(fake.address())
print(fake.phone_number())
print(fake.url())
print(fake.date())
print(fake.date_time())
print(fake.company())
print(fake.city())


