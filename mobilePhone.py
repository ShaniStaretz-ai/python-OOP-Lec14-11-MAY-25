class MobilePhone:
    def __init__(self, _brand, _color, _battery):
        print("new Mobile Phone was created")
        self.brand: int = _brand
        self.color: str = _color
        self.battery: int = _battery
