'''
-> в Python используется для аннотации типов возвращаемого значения функции. Он указывает, какой тип данных ожидает
функция для возврата, что улучшает читаемость кода, но не влияет на его выполнение. Сам по себе -> — это не оператор,
а синтаксическая конструкция для аннотирования типов

return в Python — это ключевое слово, которое используется внутри функции для завершения её выполнения и
возврата значения вызывающей стороне. Это позволяет использовать результат работы функции в других частях программы,
а не просто выводить его на экран. Если функция не имеет явного return или он пуст, она по умолчанию возвращает значение None.
'''
class Car:
    def __init__(self, number: str, model: str, color: str, horsepower: int):
        self.number = number
        self.model = model
        self.color = color
        self.horsepower = horsepower

    def util_tax(self) -> float:
        return 5000 + self.horsepower * 20

    def transport_tax(self) -> float:
        return self.horsepower * 15

    def show_info(self):
        print(f"Машина: {self.model} ({self.color}), гос.номер {self.number}, "
              f"л.сил: {self.horsepower}, утиль-сбор: {self.util_tax()}, "
              f"транспортный налог: {self.transport_tax()}")