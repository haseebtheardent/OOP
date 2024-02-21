class Tiger:
    # def __init(self) -> None:
    #     ...
    def __init__(self, tiger_age, tiger_gender, tiger_color, tiger_breed, tiger_mood) -> None:
        self.tiger_age = tiger_age
        self.tiger_gender = tiger_gender
        self.tiger_color = tiger_color
        self.tiger_breed = tiger_breed
        self.tiger_mood = tiger_mood

    # def tiger_attributes(self, tiger_age, tiger_gender, tiger_color, tiger_breed, tiger_mood):
    #     self.tiger_age = tiger_age
    #     self.tiger_gender = tiger_gender
    #     self.tiger_color  = tiger_color
    #     self.tiger_breed  = tiger_breed
    #     self.tiger_mood   = tiger_mood

    def our_tiger(self, tiger_name, tiger_diet_plan, tiger_env, tiger_outing):
        self.tiger_name = tiger_name
        self.tiger_diet_plan = tiger_diet_plan
        self.tiger_env = tiger_env
        self.tiger_outing = tiger_outing

    def tiger_memory_address(self):
        print(f'Tiger is located in {id(self)} address')

    def tiger_reports(self):
        print(f'''
Tiger Name is   {self.tiger_name}
Tiger Diet Plan  {self.tiger_diet_plan}
Tiger Gender  {self.tiger_gender}
''')

# jack : Tiger = Tiger()
# jack.tiger_attributes('2  Months','Male','Mustard','Chicken','Aggressive')
# jack.our_tiger('Jaguar','3/3','Garden','Commercial Market')
# jack.tiger_reports()
# print(f'Jack Address is {id(jack)}')
# jack.tiger_memory_address()
# rose : Tiger = Tiger()
# rosee : Tiger = Tiger()
# print(f'Rose Address is {id(rose)}')
# rose.tiger_memory_address()


david: Tiger = Tiger('2  Months', 'Male', 'Mustard', 'Chicken', 'Aggressive')
david.tiger_name = 'David'
david.tiger_diet_plan = '3 / 3'
david.tiger_reports()
