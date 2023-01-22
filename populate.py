import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')

import django
django.setup()

from app1.models import Employee

from faker import Faker
from random import randint

fake = Faker()

def populate(value):
    for i in range(value):
        feno = randint(1001,1999)
        fename = fake.name()
        fesal = randint(10000, 5000000)
        faddr = fake.city()
        emp_records = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=faddr)

def main():
    no = int(input('Enter the number of records do u wants to create:'))
    populate(no)

if __name__ == '__main__':
    main()