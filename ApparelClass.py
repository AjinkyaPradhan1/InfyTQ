class Apparel:
    def __init__(self,item_id,price,item_type):
        self.__item_id = ['C101','C102','C103','C104','S101','S102','S103','S104']
        self.__price = price
        self.__item_type = item_type
        self.counter = 100

    def set_item_id(self,item_id):
        self.__item_id = item_id

    def set_price(self,price):
        self.__price = price

    def set_item_type(self,item_type):
        self.__item_type = item_type

    def get_item_id(self):
        return self.__item_id

    def get_price(self):
        return self.__price

    def get_item_type(self):
        return self.__item_type

    def calculate_price(self):
        self.__price *= (0.05*self.__price)
        return self.__price

class Cotton(Apparel):
    def __init__(self,price,discount):
        super.__init__(price,"Cotton")
        self.__discount = discount

    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        price -= price*(0.1*self.get_price())


class Silk(Apparel):
    def __init__(self,price,discount,points):
        super.__init__(price,"Silk")
        self.__discount = discount
        self.__points = points

    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        price -= price*(0.1*self.get_price())

        if(self.__price>10000):
            self.__points = 10
        else:
            self.__points = 3
    
    def get_points(self,get_points):
        return self.__get_points