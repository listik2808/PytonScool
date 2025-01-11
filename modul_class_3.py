class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        if new_floor >self.number_of_floors  or new_floor < 1:
            print("Такого этажа не существует")
        else:
            count = 0
            while count < new_floor:
                count+=1
                print(count)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"{self.name},кол-во этажей:{self.number_of_floors}"

    def __eq__(self,other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif(isinstance(other,int)):
            return self.number_of_floors >= other

    def __lt__(self,other):
        return  self.number_of_floors < other.number_of_floors

    def __le__(self,other):
        return  self.number_of_floors <= other.number_of_floors

    def __gt__(self,other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return  self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return  self.number_of_floors != other.number_of_floors

    def __add__(self,value):
        if isinstance(value,int):
            self.number_of_floors +=value
            return self
        elif(isinstance(value,House)):
            self.number_of_floors += value.number_of_floors
            return self

    def __iadd__(self, value):
        return self.__add__(self,value)

    def __radd__(self, value):
        return self.__add__(self, value)


h1 = House("ЖК Первомайский",8)
h2 = House("Частный дом",1)
# __str__
print(h1)
print(h2)

#__len__
print(len(h1))
print(len(h2))

# __eq__
print(h1 == h2)
# __it__
print(h1 > h2)
# __lt__
print(h1 <= h2)
# __gt__
print(h1 > h2)
# __ge__
print(h1 >= h2)
# __ne__
print(h1 != h2)
# __add__
h1 = h1 + 10
print(h1)
# __iadd__
h1 + 10
print(h1)
# __radd__
h2 = h2 + 10
print(h2)
#h1.go_to(5)
#h2.go_to(10)