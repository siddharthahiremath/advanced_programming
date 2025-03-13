class Person():
    def __init__(self, name:str, age:int, height:int):
        self.name = name
        self.age = age
        self.height = height
    def loginfo(self):
        print('Name:')
        print(self.name)
        print('Age:')
        print(self.age)
        print('Height:')
        print(self.height)