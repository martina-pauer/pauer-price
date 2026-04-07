#!/usr/bin/python3
from mods.network import Connection
from mods.data import Price
from mods.data import Quality
from mods.products import Product
from mods.webpauer import WebPauer
from flask import Flask
import json

def make_load(file_name: str) -> str:
    '''
        Give the text from a file
    '''
    text: str = ''
    with open(file_name, 'r') as reading:
        text += reading.readline()
    return text

prefix: str = '/workspaces/pauer-price/src/rules/tango/'

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
##########################################################
# Define products and qualities
product_object = Product()
price_object = Price()
quality_object = Quality()
# Config objects
product_object.set_name('[ Fixing Test Product Getting ]')
price_object.set_price(1)
quality_object.set_prop('Product Property', 5)
quality_object.set_prop('Other', 3)
# Add product configured with price and quality prop
product_object.add_relation(price_object, quality_object)
# Reconfigure objects and add new product
product_object.set_name('[NEW]')
price_object.set_price(5)
quality_object.set_prop('Material', 3)
# Add New Product
product_object.add_relation(price_object, quality_object)
# When Get All Options Add to App Product Stack
app.add_product(product_object)
# Free Out RAM of Uneeded Object
del product_object, price_object, quality_object
##########################################################
# Found better product
checks: list[Product] = app.get_products()
# Send all options to first position and get better from the first
for position in range(1, checks.__len__() - 1):
    better: list[Price, Quality] = checks[position].get_better_option()
    checks[0].add_relation(better[0], better[1])
    del better
# Show in the web app which option is better
better: Product = Product()
selection: list[list[Price], list[Quality]] = checks[0].get_better_option()
del checks
better.add_relation(selection[0], selection[1])
del selection
connector.send_data('{' + f'{better.get_prices()[0]}, {better.get_quality()[0]}' + '}')
app.add_connection(connector)
app.add_view(weba)