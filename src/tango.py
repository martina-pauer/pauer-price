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

prefix: str = 'rules/tango/'

verify: str = make_load(f'{prefix}connection.json')
send: str = make_load(f'{prefix}sending.json')
answer: str = make_load(f'{prefix}response.json')

del prefix
    
connector: Connection = Connection()
app: WebPauer = WebPauer

if __name__ == '__main__':
    # Make the connection after change API_access_token written in the web app
    connector.connect('https://tiendas.axoft.com/api/Aperture/dummy', connector.API_access_token)
    # Check each product and get price
    app.read_from_user('formText')
    # Found better product
    checks: list[Product] = app.get_products()
    # Send all options to first position and get better from the first
    for position in range(1, checks.__len__() - 1):
        better: list[list[Price], list[Quality]] = checks[position].get_better_option()
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
    weba = Flask(__name__)
    app.add_view(weba)
    weba = app.view()