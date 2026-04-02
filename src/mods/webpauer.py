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
        self.app_name = give_name

    def set_style(self, URL: str):
        '''
            Add styles to the Web App.
        '''
        self.stylesheet_URL = URL

    def add_connection(self, conn: Connection):
        '''
            Make connection to an API based on
            JSON.
        '''
        self.connector = conn
        # Select access token from form and API URL from the object
        self.connector.connect(conn.URL, self.read_from_user('formText'))

    def add_product(self, prod: Product):
        '''
            Define a new product for the
            app.
        '''
        if self.products.__len__() >= 3:
            self.products.append(prod)
        else:
            # Save asignaction and only copy needed data to empty Product object slot
            product_object = self.products[self.products.__len__() - 1]
            product_object.product_name = prod.get_name()
            product_object.add_relation(prod.get_prices()[0], prod.get_quality()[0])

    def read_from_user(self, category: str):
        '''
            Get data from forms that user
            complete in the app, files from
            the device, cookies, sensors and
            any data that is get of different
            way category dependant:

            Categories
            
                - 'formText': data from text entry form
                - 'devFile': file from user device
                - 'formOption': selected option from menu
                - 'getTemp': device temperature sensor
                - 'cam': WebCam from user
                - 'mic': User audio Microphone 
        '''
        # Detition map for optimize choose one app part by category of data input
        get_category: dict[str, str] =  {
                            'formText': self.user_inputs.__setitem__(category, '[TOKEN FROM NEXT ENTRY IN WEB FORM]'),
                            'devFile': self.user_inputs.__setitem__(category, '[CONTENT FROM FILE]'),
                            'formOption': self.user_inputs.__setitem__(category, ''),
                            'cam': self.user_inputs.__setitem__(category, ''),
                            'mic': self.user_inputs.__setitem__(category, ''),
                            'getTemp': self.user_inputs.__setitem__(category, '')
                        }
        # Save input in dictionary each one is used for selected category use different app parts
        get_category.get(category)
        
    def get_name(self) -> str:
        '''
            Said what name has the Web App.
        '''
        return self.app_name

    def get_products(self) -> list[Product]:
        '''
            Give list with the Product objects
            that represents the products from
            the Web App.
        '''
        return self.products

    def get_last_JSON(self) -> str:
        '''
            Give the last JSON response from
            connected API.
        '''
        self.connector.get_response()