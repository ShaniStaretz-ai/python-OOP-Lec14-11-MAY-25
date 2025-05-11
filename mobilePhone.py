class MobilePhone:
    def __init__(self, _brand, _mode, _color, _battery):
        print("new Mobile Phone was created")
        self.brand: int = _brand
        self.mode: int = _mode
        self.color: str = _color
        self.battery: int = _battery

    def __str__(self) -> str:
        # return  str(self.__dict__)
        return (f"Mobile Information:\n"
                f"Brand:{self.brand}\n"
                f"Mode:'{self.mode}'\n"
                f"color:{self.color}\n"
                f"battery:{self.battery}\n")

    def __repr__(self):
        return f"MobilePhone('{self.brand}','{self.mode}','{self.color}',{self.battery}')"
