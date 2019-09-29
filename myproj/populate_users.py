import sys
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'myproj.settings')

import django
django.setup()

from appTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_firstname = fake_name[0]
        fake_lastname = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(
        first_name=fake_firstname,last_name=fake_lastname,email=fake_email
        )[0]

if __name__ == '__main__':
    print("populating user")
    populate(20)
    print("DONE")