from mobilePhone import MobilePhone
from person import Person

if __name__ == '__main__':
    samsung = MobilePhone('samsung', 'S25Ultra','black', 25)
    iphone = MobilePhone('Iphone', '16pro','white', 25)
    dany = Person(1, 'Dany', 190, 30_000)
    print(dany)# will print the object attributes
    bag:list[MobilePhone]=[samsung,iphone]
    print("__repr__ list:",bag)
    print("__repr__ dev code:",samsung.__repr__())

