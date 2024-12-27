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

h1 = House("ЖК Первомайский",8)
h2 = House("Частный дом",1)
h1.go_to(5)
h2.go_to(10)