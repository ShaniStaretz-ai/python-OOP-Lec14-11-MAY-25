from typing import override
class Person:
    def __init__(self, _id, _name, _height,_salary):
        print("new Person was created")
        self.id:int = _id
        self.name:str = _name
        self.height:float = _height
        self.salary:int=_salary

    @override
    def __str__(self)->str:
        # return  str(self.__dict__)
        return (f"Person Information:\n"
                f"ID:{self.id}\n"
                f"Name:'{self.name}'\n"
                f"Height:{self.height}\n"
                f"Salary:{self.salary}\n")

if __name__ == '__main__':
    print(Person.__dict__)
