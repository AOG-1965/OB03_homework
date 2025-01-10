# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

    def make_sound(self):   # возвращает общий звук для всех животных
        return "Животное издает звук"

    def eat(self):          # выводит, что животное ест
        return f"{self.name} ест."