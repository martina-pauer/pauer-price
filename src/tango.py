#!/usr/bin/python3
from mods.network import Connection
from mods.data import Price
from mods.data import Quality
from mods.products import Product
from mods.webpauer import WebPauer
from flask import Flask
import json
import random

def make_load(file_name: str) -> str:
    '''
        Give the text from a file
    '''
    text: str = ''
    with open(file_name, 'r') as reading:
        text += reading.readline()
    return text

prefix: str = './rules/tango/'

verify: str = make_load(f'{prefix}connection.json')
send: str = make_load(f'{prefix}sending.json')
answer: str = make_load(f'{prefix}response.json')

del prefix
    
connector: Connection = Connection()
app: WebPauer = WebPauer()
weba: Flask = Flask(__name__)
# Tango Web App
# Make the connection after change API_access_token written in the web app
connector.connect('https://tiendas.axoft.com/api/Aperture/dummy', connector.API_access_token)
# Check each product and get price
app.read_from_user('formText')
# Get Price, Product Name and list of tuples with Property Name or Score from API data
###########################
API_DATA: list[tuple] = []
for product_name in range(1, 11):
    product_tuple = (random.randint(1, 20), f'Product {product_name}', [])
    # Get Properties With Score and add to props tuple list
    prop = (f'Property {chr(random.randint(33, 126))}', random.randint(1, 10))
    product_tuple[2].append(prop)
    del prop
    # Add to tuples list the products data tuple
    API_DATA.append(product_tuple)
    # Free memory when end loop for doesn't use more memory
    del product_tuple    
# Free module used by module when is not needed    
del random
###########################
# List with price, product name, props tuples list
for product_data in API_DATA:
    # Define products and qualities
    product_object = Product()
    price_object = Price()
    quality_object = Quality()
    # Config objects
    product_object.set_name(product_data[1])
    price_object.set_name(product_object.get_name())
    quality_object.set_name(product_object.get_name())
    price_object.set_price(product_data[0])
    for props in product_data[2]:
        # Iterates over the tuple list with property name and score
        quality_object.set_prop(props[0], props[1])
    # Add product configured with price and quality prop
    product_object.add_relation(price_object, quality_object)
    app.add_product(product_object)
    # When Get All Options Add to App Product Stack
    # Free Out RAM of Uneeded Object
    del product_object, price_object, quality_object
# Delete API data for protect it
del API_DATA    
# Found better product
checks: list[Product] = app.products
# Send all options to first position and get better from the first
for position in range(1, checks.__len__()):
    better: list[Price, Quality] = checks[position].get_better_option()
    checks[0].add_relation(better[0], better[1])
    del better
# Show in the web app which option is better
better: Product = Product()
selection: list[Price, Quality] = checks[0].get_better_option()
del checks
better.add_relation(selection[0], selection[1])
del selection
connector.send_data('{' + f'{better.get_prices()[0]}, {better.get_quality()[0]}' + '}')
# Listen Port for make the app public with npx
weba.run(host = '0.0.0.0', port = 5000, debug = True)
app.add_view(weba)