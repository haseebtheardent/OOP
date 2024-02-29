class HRJ:
    def __init__(self, shirts, pants, hoodies, coats):
        self.shirts = shirts
        self.pants = pants
        self.hoodies = hoodies
        self.coats = coats

    def add_shirts(self, quantity):
        self.shirts += quantity

    def add_pants(self, quantity):
        self.pants += quantity

    def add_hoodies(self, quantity):
        self.hoodies += quantity

    def add_coats(self, quantity):
        self.coats += quantity

    def remove_shirts(self, quantity):
        if self.shirts >= quantity:
            self.shirts -= quantity
        else:
            print("Error: Insufficient quantity of shirts.")

    def remove_pants(self, quantity):
        if self.pants >= quantity:
            self.pants -= quantity
        else:
            print("Error: Insufficient quantity of pants.")

    def remove_hoodies(self, quantity):
        if self.hoodies >= quantity:
            self.hoodies -= quantity
        else:
            print("Error: Insufficient quantity of hoodies.")

    def remove_coats(self, quantity):
        if self.coats >= quantity:
            self.coats -= quantity
        else:
            print("Error: Insufficient quantity of coats.")

    def display_inventory(self):
        print("Inventory:")
        print("Shirts:", self.shirts)
        print("Pants:", self.pants)
        print("Hoodies:", self.hoodies)
        print("Coats:", self.coats)


hrj_store = HRJ(shirts=50, pants=30, hoodies=20, coats=10)
hrj_store.display_inventory()

hrj_store.add_shirts(10)
hrj_store.add_pants(5)
hrj_store.remove_hoodies(3)

hrj_store.display_inventory()
