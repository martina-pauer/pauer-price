#!/usr/bin/python3
from mods.network import Connection
from mods.data import Price, Quality
from mods.products import Product
from flask import Flask
from flask import request

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

if __name__ == '__main__':
    # Make the connection after change API_access_token written in the web app
    connector.connect('https://tiendas.axoft.com/api/Aperture/dummy', connector.API_access_token)
    # Check each product and get price
    # Found better product
    # Show in the web app which option is better