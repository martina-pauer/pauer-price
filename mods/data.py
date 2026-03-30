class Quality:
    '''
        Setting a Quality reference for a product
        with custom properties to estimate quality 
        numeric score from 1 to 10.
    '''
    def __init__(self):
        
        self.product_name: str = ''

        self.properties: dict[str, int] = {}

    def set_name(self, product: str):
        '''
            Give name for product with this
            quality
        '''
        self.product_name = product 

    def set_prop(self, property_name: str, score: int):
        '''
            Add a new property with his respective score
            for it from 1 to 10.

            The object could be until ten customs
            properties.
        '''
        if  (
                (not self.properties.keys().__contains__(property_name)) 
                and ((score >= 1) and (score <= 10))
            ):
            # Prevent from overwrite existents values and score out range
            self.properties.__setitem__(self.product_name, score)

    def get_name(self) -> str:
        '''
            Return the name setted for this
            quality option.
        '''
        return self.product_name

    def get_props(self) -> dict[str, int]:
        '''
            Retrun the dictionary with custom
            properies and his respective score
            for analyze this quality option
        '''
        return self.properties

    def calc(self) -> int:
        '''
            Use all properties scores for
            estimate a average score to all
            quality from 1 to 10
        '''    
        score: int = 0

        for prop in self.properties.keys():
            # As all prop scores must have 1 to 10
            # then score be greater than 1 to 10
            score += self.properties[prop]
        # Calc integer average (until 10 properties is recommended)
        score //= self.properties.keys().__len__()

        return score    
    
class Price:
    '''
        Define pricing option for a product.
    '''    
    def __init__(self):
        pass    