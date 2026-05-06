from flask import request
from mods.network import Connection
from mods.products import Product
from mods.products import Quality
from mods.data import Price

class WebPauer:
    '''
        Define basic structure with a
        simple web app with forms and
        views
    '''
    def __init__(self):
        
        self.app_name: str = 'Web Pauer'

        self.user_inputs: dict[str, str] = {}

        self.stylesheet_path: str = '/workspaces/pauer-price/src/web/test.css'

        self.connector: Connection = Connection()

        self.products: list[Product] = [Product(), Product()]

        self.view = None

    def set_name(self, give_name: str):
        '''
            Add a name for the Web App.
        '''
        self.app_name = give_name

    def set_style(self, path: str):
        '''
            Add styles to the Web App
            from local CSS file.
        '''
        self.stylesheet_path = path

    def add_connection(self, conn: Connection):
        '''
            Make connection to an API based on
            JSON.
        '''
        self.connector = conn
        # Select access token from form and API URL from the object
        self.connector.connect(conn.URL, self.uncrypt(self.connector.API_access_token))

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
                            'formText': self.user_inputs.__setitem__(category, self.get_text_input(1)),
                            'devFile': self.user_inputs.__setitem__(category, ''),
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

    def get_text_input(self, input_number: int) -> str:
        '''
            Get Value from numbered "input_" 
            text input in the page form
        '''
        input_name: str = f'input_{input_number}'
        
        try:
            return self.user_inputs['formText']
        except:
            return 'Input doesn\'t exist'

    def add_view(self, obj):
        self.view = obj

        @self.view.route('/', methods = ['GET', 'POST'])
        def show() -> str:
            
            page: str = ''
            input_number: int = 1
            
            with open('/workspaces/pauer-price/src/web/index.html', 'r') as text:
                for line_text in text.readlines():
                    # Get data from a hypertext document for make the page
                    # Only replace when found replacing line after only add text for more velocity
                    if line_text.__contains__('CSS'):
                        css_content = ''
                        with open(self.stylesheet_path, 'r') as container:
                           for line in container.readlines():
                                # Make this for read all lines not only the first
                                css_content += line
                        # Add code for styles in <style> tag HTML document section        
                        line_text = line_text.replace('[CSS CODE]', css_content)
                        # Make two actions, one of this conditionals and adding HTML to the view
                    else:    
                        # After style change line_text value by his text replacing input for a writing field
                        entry_name: str = f'input_{input_number}'
                        if line_text.__contains__('[INPUT]'):
                            # Only count when add new input for don't turn it very great
                            input_number += 1
                            # Scape single quotes for work better
                            line_text = line_text.replace('[INPUT]', f'<input id = "{entry_name}" name = "input_1" type = "text" onchange = \'javascript: maskData("{entry_name}");\' />')
                        del entry_name
                        if line_text.__contains__('[JSON]'):
                            aux_text: str = ''
                            # Load Text from JSON inside javascript for work well the encrypting
                            with open('./web/encrypt.json') as lines:
                                # Run in Context of src folder instead of src/mods folder
                                for line in lines.readlines():
                                    # Erase newlines and tabs in the file to use code format
                                    aux_text += line.replace('\n', '').replace('\t', '')
                            # Replace JSON template by content
                            line_text = line_text.replace('[JSON]', aux_text)
                            del aux_text
                    # Always add line_text don't matter modification    
                    page += line_text     
            # When get all the HTML text show input_1 value with post
            if request.method == 'POST':
                # Get data
                self.user_inputs.__setitem__('formText', request.form['input_1'])  
                # Use Encrypted text only need uncrypt when is used when add connection
                self.connector.API_access_token = self.user_inputs['formText']
                self.add_connection(self.connector)
                # Show data only when get Token
                better: list[Price, Quality] = self.get_products()[0].get_better_option()
                page = page.replace('Write Tango API Access Token to Products Lists...', f'Product <span>{better[0].get_name()}</span> to ${better[0].get_price()} with scored quality {better[1].calc()}.')
                del better
                
            return page

    def uncrypt(self, coded_message: str) -> str:
        '''
            Method for flexible encryption with
            temporal duration only when is needed
        ''' 
        import json
        # Use load method that get as input a file handler object to gets well the text
        inverse_relation: dict = json.load  (
                                                open('./web/encrypt.json', 'r')
                                            )
        # Reverse Dictionary
        aux: dict = {}
        
        for replacing in inverse_relation.keys():
            # Send Value to Key and key to value
            aux.__setitem__(inverse_relation[replacing], replacing)
        # Save in inverse_relation the inverse dictionary
        inverse_relation: dict = aux
        del aux
        # Follow with the uncrypting algorithm    
        relation_keys: dict[str, str] = inverse_relation.keys()
        uncrypted_text: str = coded_message
        # Replacing the encrypted for equivalence using inverse relation to javascript dict
        for uncrypt in relation_keys:
            uncrypted_text: str = uncrypted_text.replace(uncrypt, inverse_relation[uncrypt])
        return uncrypted_text       