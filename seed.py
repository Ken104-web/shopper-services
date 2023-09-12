from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Customer, Product, Service
from faker import Faker
import random

engine = create_engine('sqlite:///shoppers.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

items = ["Bread", "Milk", "Eggs", "Fresh fruits", "Fresh vegetables", "Cereal", "Pasta", "Rice", "Canned soup", "Peanut butter", "Bottled water", "Snack chips", "Frozen pizza", "Ground beef", "Toilet paper", "Laundry detergent", "Toothpaste"]


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

    print('seeding services')
    for i in range(17):
        servant_name = Service(servant=fake.name(), rating= fake.random_number(digits=1))
        session.add(servant_name)
        session.commit()

        print('***service seeding done***')

    print('seeding products')
    for customer in customers:
        products = [Product(product_name=items[i % len(items)], price=fake.random_number(digits=2), customer_id=customer.id, service_id=random.randint(0, 9)) for i in range(17)]
        session.add_all(products)
        session.commit()
        print("seeding done")










