import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Customer, Product, Service

engine = create_engine('sqlite:///shoppers.db')
Session = sessionmaker(bind=engine)
session = Session()
while True:
    text = 'Ujenzi supermarket!'
    click.echo(text)
    @click.group()
    def cli():
        "Thank you for shopping at Ujenzi Supermarket"

  
    @cli.command()
    # calling customer commandlist
    def display_customers():
        click.echo(f'Here is a list of customer: ')
        list_customers = session.query(Customer).all()
        for customer in list_customers:
                click.echo(f"{customer.id}, Name: {customer.name}")

   
        def call_customer(id):
            # call a specific customer
            customer = session.query(Customer).filter_by(id=id).first()
            if customer: 
                click.echo(f"Customer Name: {customer.name}")
            else:
                click.echo(f"Customer not found")
                
        name = click.prompt('\nEnter the name of the customer:')
        call_customer(name)

        def product_name(id):
            customer_product = session.query(Product).filter_by(id=id).first()
            if customer_product:
                click.echo(f'Products purchased: {customer_product.product_name}')
            else:
                click.echo(f"Product doesn't match")
        
        product = click.prompt('\nEnter the bought product:')
        product_name(product)

        



    break

if __name__ == '__main__':
    cli()





