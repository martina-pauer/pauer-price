from data import Price
from data import Quality

class Product:
    def __init__(self):
        '''
            Define the kind of product and the relation
            for get the better options more economic
        '''
        self.product_name: str = ''

        self.prices: list[Price] = []

        self.qualities: list[Quality] = []

    def add_relation(self, price: list[Price], quality: list[Quality]):
        '''
            Add a new option with the price and his respective
            quality for the product.
        '''
        if not (self.prices.__contains__(price) and self.qualities.__contains__(quality)):
            # Only add when the option is new for optimeze from 2 to 1 when is not need
            self.prices.append(price)
            self.qualities.append(quality)

    def get_better_option(self) -> list[list[Price], list[Quality]]:
        '''
            Get the Great quality to minor price
        '''
        minor_price: int = self.prices[0].price
        major_quality: int = self.qualities[0].calc()
        better_price_object: list[Price] = self.prices[0]
        better_quality_object: list[Quality] = self.qualities[0]

        for option in range(1, self.prices.__len__()):
            # Compare the before with after prices and qualies
            quality_calc: int = self.qualities[option].calc()
            if  (
                    (self.prices[option].price < minor_price) 
                    and (quality_calc > major_quality)
                ):
                # Get both price and quality
                major_quality: int = quality_calc
                del quality_calc
                # Update new object that follow the requirements
                better_price_object: list[Price] = self.prices[option]
                minor_price: int = better_price_object.price
                better_quality_object = self.qualities[option]

        del minor_price, major_quality
        
        return [better_price_object, better_quality_object]           
    
    def get_name(self) -> str:
        '''
            Give the product name.
        '''
        return self.product_name   

    def get_prices(self) -> list[Price]:
        '''
            Give the list with the objects
            than represent the different
            optional prices for the product.
        '''
        return self.prices  

    def get_quality(self) -> list[Quality]:
        '''
            Give the list with the object
            than represent the different
            optional quality for the product.
        '''
        return self.qualities