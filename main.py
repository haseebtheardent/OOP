class Tiger:
    def __init__(self):
        pass

    def set_attributes(self, age, color, gender, breed, mood):
        self.Tiger_age = age
        self.Tiger_color = color
        self.Tiger_gender = gender
        self.Tiger_breed = breed
        self.Tiger_mood = mood

    def set_details(self, name, diet_plan, outing, environment):
        self.tiger_name = name
        self.tiger_diet_plan = diet_plan
        self.tiger_outing = outing
        self.tiger_env = environment

    def __str__(self):
        return f"Tiger(name={self.tiger_name}, age={self.Tiger_age}, color={self.Tiger_color}, gender={self.Tiger_gender}, breed={self.Tiger_breed}, mood={self.Tiger_mood}, diet_plan={self.tiger_diet_plan}, outing={self.tiger_outing}, environment={self.tiger_env})"

    def get_memory_address(self):
        print(f'Tiger is located at memory address: {id(self)}')

    def tiger_report(self):
        print(f'''
        Tiger Report:
        Tiger name: {self.tiger_name}
        Tiger diet plan: {self.tiger_diet_plan}
        Tiger Environment: {self.tiger_env}
        ''')

obj1 = Tiger()
obj1.set_attributes('2 Months', 'black', 'male', 'chicken', 'aggressive')
obj1.set_details('jack', '3 / 3', 'Commercial', 'garden')
obj1.get_memory_address()
obj1.tiger_report()
print(f'obj1 Address is {id(obj1)}')
