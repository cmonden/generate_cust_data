from faker import Faker
import csv

fake = Faker()

# Generate 1000 customer records
customers = []
for i in range(1000):
    customer = {}
    customer['name'] = fake.name()
    customer['email'] = fake.email()
    customer['phone'] = fake.phone_number()
    customer['street'] = fake.street_address()
    customer['city'] = fake.city()
    customer['state'] = fake.state()
    customer['zip'] = fake.postcode()
    customers.append(customer)

# Write customer records to a CSV file
with open('customers.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'email', 'phone', 'street', 'city', 'state','zip'])
    writer.writeheader()
    for customer in customers:
        writer.writerow(customer)
