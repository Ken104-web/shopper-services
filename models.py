from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///shoppers.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
# created a many to many table relationship of customer_service
customer_service = Table('customer_service', Base.metadata, Column('customer_id', ForeignKey('customers.id'), primary_key =True), Column('service_id', ForeignKey('services.id'), primary_key=True))

# creating the models
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    # one to many with products
    products = relationship('Product', backref=backref('customer_name'))

    # many to many with service
    services = relationship('Service', secondary=customer_service, back_populates = 'customers')




class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer(), primary_key = True)
    servant = Column(String())
    rating = Column(Integer())

    # one to many with product
    products = relationship('Product', backref=backref('services_too'))

    # many to many with customer
    customers = relationship('Customer', secondary=customer_service, back_populates = 'services')


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer(), primary_key = True)
    price = Column(Integer())
    product_name = Column(String())
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    service_id = Column(Integer(), ForeignKey('services.id'))


