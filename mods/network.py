class Connection:
    '''
        Define conection abstraction
        for JSON based API
    '''
    def __init__(self):
        
        self.URL: str = 'https://'
        
        self.API_access_token: str = 'XXXXXX'

        self.JSON_sended: str = 'Sending...'

        self.JSON_response: str = 'Waiting...'

    def connect(self, URL: str, token: str):
        '''
            Make connection using POST method
            to the API with the URL 
            and API Access Token.
        '''
        self.URL = URL
        self.API_access_token = token
        # Establish connection to API waitng for JSON requests

    def send_data(self, request: str):
        '''
            Send orders to API in JSON format.
        '''
        self.JSON_sended = request

    def get_response(self) -> str:
        '''
            Give the received from API
            data in JSON format.
        '''
        return self.JSON_response