from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Customer, Product, Service
from faker import Faker
import random

engine = create_engine('sqlite:///shoppers.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

items = ["Bread"
"Milk"
"Eggs"
"Fresh fruits"
"Fresh vegetables"
"Cereal"
"Pasta"
"Rice"
"Canned soup"
"Peanut butter"
"Bottled water"
"Snack chips"
"Frozen pizza"
"Ground beef"
"Toilet paper"
"Laundry detergent"
"Toothpaste"]

if __name__ == '__main__':
    print('Clearing DB******')
    session.query(Customer).delete()
    session.query(Product).delete()
    session.query(Service).delete()
    print('Done')

    print('seeding customers***')
    customers = []
    for i in range(17):
        new_customer = Customer(name=fake.name())
        session.add(new_customer)
        session.commit()
        customers.append(new_customer)
    print('seeded customers')

    





