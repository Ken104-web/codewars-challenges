from app import app
from models import db, Customer


with app.app_context():
    Customer.query.delete()


    print('Seeding data..')
    customer1 = Customer(
            first_name='Jared',
            last_name='ely',
            email='jared.ely@sakilacustomer.org'
            )
    customer2 = Customer(
            first_name='Mary',
            last_name='Smith',
            email='mary.smith@sakilacustomer.org'
            )
    customer3 = Customer(
            first_name='Patricia',
            last_name='Johnson',
            email=' patricia.johnson@sakilacustomer.org'
            )

    db.session.add_all([customer1, customer2, customer3])
    db.session.commit()
    print('***done**')






