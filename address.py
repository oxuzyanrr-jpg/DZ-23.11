'''
Напоминания для себя!
name: str, age: int, group: str — это type hints (подсказки типов). Они не обязательны, но помогают IDE и статическим анализаторам.
'''
class Address:
    def __init__(self, city: str, street: str, house: str, flat: int):
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def show_info(self):
        print(f"Адрес: г.{self.city}, ул.{self.street}, д.{self.house}, кв.{self.flat}")
