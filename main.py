# class Tiger:
#     def Tiger_attributes(self, Tiger_age, Tiger_color, Tiger_gender, Tiger_breed, Tiger_mood):
#         self.Tiger_age = Tiger_age
#         self.Tiger_color = Tiger_color
#         self.Tiger_gender = Tiger_gender
#         self.Tiger_breed = Tiger_breed
#         self.Tiger_mood = Tiger_mood


# def our_tiger(self, tiger_name, tiger_diet_plan, tiger_outing, tiger_env):
#     self.tiger_name = tiger_name
#     self.tiger_diet_plan = tiger_diet_plan
#     self.tiger_outing = tiger_outing
#     self.tiger_env = tiger_env


# def tiger_memory_address(self):
#     print(f'Tiger is located in this {id(self)} address')


# def tiger_report(self):
#     print(f'''
#     Tiger Report is
#     Tiger name is {self.tiger_name}
#     Tiger diet plan is {self.tiger_diet_plan}
#     Tiger Environment is {self.tiger_env}
#     ''')

#     obj1: Tiger = Tiger()
#     obj1.Tiger_attributes('2 Months', 'black', 'male', 'chicken', 'agressive')
#     obj1.our_tiger('jack', '3 / 3', 'Commercial', 'garden')
#     obj1.tiger_memory_address()
#     obj1.tiger_report()
#     print(f'obj1 Address is {id(obj1)}')


# Chat GPT
class Tiger:
    def Tiger_attributes(self, Tiger_age, Tiger_color, Tiger_gender, Tiger_breed, Tiger_mood):
        self.Tiger_age = Tiger_age
        self.Tiger_color = Tiger_color
        self.Tiger_gender = Tiger_gender
        self.Tiger_breed = Tiger_breed
        self.Tiger_mood = Tiger_mood

    def our_tiger(self, tiger_name, tiger_diet_plan, tiger_outing, tiger_env):
        self.tiger_name = tiger_name
        self.tiger_diet_plan = tiger_diet_plan
        self.tiger_outing = tiger_outing
        self.tiger_env = tiger_env

    def tiger_memory_address(self):
        print(f'Tiger is located in this {id(self)} address')

    def tiger_report(self):
        print(f'''
        Tiger Report is
        Tiger name is {self.tiger_name}
        Tiger diet plan is {self.tiger_diet_plan}
        Tiger Environment is {self.tiger_env}
        ''')


obj1 = Tiger()
obj1.Tiger_attributes('2 Months', 'black', 'male', 'chicken', 'aggressive')
obj1.our_tiger('jack', '3 / 3', 'Commercial', 'garden')
obj1.tiger_memory_address()
obj1.tiger_report()
print(f'obj1 Address is {id(obj1)}')
