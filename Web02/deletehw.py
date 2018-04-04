import mlab
from mongoengine import *
from models.customer import Customer

mlab.connect()

id_to_find = "5ac4e37b0e961727086293c0"

Customer.objects(id=id_to_find).delete()
