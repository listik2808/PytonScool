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

h1 = House("ЖК Первомайский",8)
h2 = House("Частный дом",1)
# __str__
print(h1)
print(h2)

#__len__
print(len(h1))
print(len(h2))



#h1.go_to(5)
#h2.go_to(10)