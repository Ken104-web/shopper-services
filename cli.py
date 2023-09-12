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
        click.echo(f'Here is a lis of customer: ')
        list_customers = session.query(Customer).all()
        for customer in list_customers:
                click.echo(f"{customer.id}, Name: {customer.name}")


    break


if __name__ == '__main__':
    cli()





