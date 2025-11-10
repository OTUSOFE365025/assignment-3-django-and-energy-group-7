############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

if Product.objects.count() == 0:
    products = [
        [ "1", "Apple",  0.99 ],
        [ "2", "Banana", 0.79 ],
        [ "3", "Chocolate", 2.49 ],
        [ "4", "Noodles", 3.29],
    ]

    for p in products:
        Product.objects.create(upc=p[0], name=p[1], price=p[2])

    print("Database filled.")

else:
    print("Database already filled.")

while True:
    user_input = input("\nEnter product UPC ('exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting Application.")
        break

    try:
        product = Product.objects.get(upc=user_input)
        print(f"\nProduct Name: {product.name}\nProduct Price: ${product.price}")
    except Product.DoesNotExist:
        print("\nProduct not found. Please try again.")