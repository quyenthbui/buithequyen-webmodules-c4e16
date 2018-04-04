from models.customer import Customer
import mlab
from faker import Faker
from random import randint,choice

fake = Faker()

mlab.connect()

for i in range(100):
    print('Saving Customer',i+1,'......')
    new_customer = Customer(name=fake.name(), gender= randint(0,1), phone=fake.phone_number(), job=fake.job(), company = fake.company() ,contacted = choice([True,False]))
    new_customer.save()
