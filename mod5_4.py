class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        # cls.name = kwargs.get('name')
        # House.houses_history.append(cls.name)
        # print(cls.name)
        print(args)
        print(kwargs)

        # House.houses_history.append(cls.name)
        return object.__new__(cls)

    def __init__(self,*args, **kwargs): # first, second, third):
        name = ''
        number_of_floors = 0
        self.args = args
        self.kwargs = kwargs
        # for key,value in kwargs.items():
        #     setattr(self,key,value)
        self.name = args[0]
        self.number_of_floors = args[1]

        House.houses_history.append(self.name)
        #self.name = kwargs.get('name')
        #self.number_of_floors = kwargs.get("number_of_floors")
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

oter =[1,2,3]
house_ = {'name':'ЖК Юбилейный', 'number_of_floors':28}
oter2 =[1,2,3]
house_2 = {'name':'ЖК Южный', 'number_of_floors':10}
h1 = House('ЖК Юбилейный', 28)

h2 = House('ЖК Южный', 10)
print(h1.args)
print(h1.kwargs)
print(h1.name)
print(h1.number_of_floors)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
print(h3.name)
del(h2)
input()

