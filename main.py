from student import Student
from car import Car
from address import Address

students = [
    Student("Анна", 19, "Б01-201"),
    Student("Иван", 20, "Б02-102"),
    Student("Марина", 18, "Б03-304")
]

cars = [
    Car("A123BC", "Toyota Camry", "черный", 181),
    Car("B777BB", "BMW 320i", "синий", 184),
    Car("X999XX", "Lada Granta", "белый", 98)
]

addresses = [
    Address("Москва", "Тверская", "10", 15),
    Address("Санкт-Петербург", "Невский", "120", 43),
    Address("Казань", "Баумана", "5", 7)
]

print("=== Студенты ===")
for s in students:
    s.show_info()

print("\n=== Машины ===")
for c in cars:
    c.show_info()

print("\n=== Адреса ===")
for a in addresses:
    a.show_info()
