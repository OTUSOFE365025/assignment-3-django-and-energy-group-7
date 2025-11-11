[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-cPJVYMd)
Django ORM Standalone
=====================

![Django](https://img.shields.io/badge/Django_ORM-Standalone-blue)
![Python](https://img.shields.io/badge/Python-yellow)

We used this Django ORM Standalone and edited to make our Cash Register Application. It is used to leverage its database operations. We have implemented a Product table and then made a program that populates the database and lets the user query the products using the UPC code.

:gear: Requirements
-------------------
- Last tested successfully with Python 3.14.0 and Django 5.2.6
- Create venv and pip install django to import the required modules.

:open_file_folder: File Structure
---------------------------------
```
django-orm/
├── db/
│   ├── __init__.py
│   └── models.py
├── main.py
├── manage.py
├── README.md
└── settings.py
```

The program is written in main.py which already has access to the products model in db/models.py. The db/models.py contains the product model and structure. The rest of the files are the regular django setup from the Django ORM Standalone.

:rocket: Quick Setup
--------------------
Create a folder for your project on your local machine
```
mkdir myproject; cd myproject
```
Create a virtual environment and install django
```
python -m venv venv; source venv/bin/activate; pip install django
```
Download this project template from GitHub
```
git clone https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-7.git; cd assignment-3-django-and-energy-group-7
```
Initialize the database
```
python manage.py makemigrations db; python manage.py migrate
```
Run the project
```
python main.py
```

:crystal_ball: Example
----------------------
After running Quick Start above: 

Code in db/models.py:
```
class Product(models.Model):
    upc = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} (${self.price})"
```
Code in main.py:
```
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
```
Output from command: ```python main.py``` and user input

<img width="748" height="283" alt="image" src="https://github.com/user-attachments/assets/5e32f715-7296-48fa-b4cf-d77aba59a3cb" />

:mortar_board: Django Models
----------------------------

Link: [How to Use Django Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)

License
-------

The MIT License (MIT) Copyright (c) 2024 Dan Caron

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
