from network import Connection
from products import Product
from data import Price

class WebPauer:
    '''
        Define basic structure with a
        simple web app with forms and
        views
    '''
    def __init__(self):
        
        self.app_name: str = 'Web Pauer'

        self.user_inputs: dict[str, str] = {}

        self.stylesheet_URL: str = 'https://'

        self.connector: Connection = Connection()

        self.products: list[Product] = [Product(), Product(), Product()]

    def set_name(self, give_name: str):
        '''
            Add a name for the Web App.
        '''
        pass

    def set_style(self, URL: str):
        '''
            Add styles to the Web App.
        '''
        pass

    def add_connection(self, con: Connection):
        '''
            Make connection to an API based on
            JSON.
        '''
        pass

    def add_product(self, prod: Product):
        '''
            Define a new product for the
            app.
        '''
        pass

    def read_from_user(self, category: str):
        '''
            Get data from forms that user
            complete in the app, files from
            the device, cookies, sensors and
            any data that is get of different
            way category dependant:

            Categories
            
                - 'formText': data from text entry form
                - '': file from user device
                - '': device temperature sensor
                - '': 
        '''
        pass

    def get_name(self) -> str:
        '''
            Said what name has the Web App.
        '''
        pass

    def get_products(self) -> list[Product]:
        '''
            Give list with the Product objects
            that represents the products from
            the Web App.
        '''
        pass

    def get_last_JSON(self) -> str:
        '''
            Give the last JSON response from
            connected API.
        '''
        pass