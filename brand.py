class HN:
    def __init__(self):
        pass

    def articles(self, shirt, pent, coat, jacket):
        self.shirt = shirt
        self.pent = pent
        self.coat = coat
        self.jacket = jacket

    def length(self, shirt_size, pent_waist, coat_size, jacket_size):
        self.shirt_size = shirt_size
        self.pent_waist = pent_waist
        self.coat_size = coat_size
        self.jacket_size = jacket_size

    def price(self, shirt_price, pent_price, coat_price, jacket_price):
        self.shirt_price = shirt_price
        self.pent_price = pent_price
        self.coat_price = coat_price
        self.jacket_price = jacket_price

    def __str__(self):
        return f'Shirt: {self.shirt}, Size: {self.shirt_size}, Price: {self.shirt_price}'    

    def get_memory_address(self):
        print(f'Memory address is {id(self)}')    

obj1 = HN()
obj1.articles("black_shirt", "black_pent", "brown_coat", "white_jacket")
obj1.length(15, 38, 17, 18)
obj1.price('15$', '13$', '50$', '100$')
obj1.get_memory_address()
print(obj1)
