import mlab
from mongoengine import *
from models.customer import Customer

mlab.connect()

id_to_find = "5ac4e37b0e961727086293c0"

find = Customer.objects.get(id=id_to_find)

print(find.name)
