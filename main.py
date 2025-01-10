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

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).

class Bird(Animal):
    def __init__(self, name, age, flight_speed):
        super().__init__(name, age)         # Вызов конструктора родительского класса
        self.flight_speed = flight_speed    # Специфический атрибут - "скорость полета"

    def make_sound(self):                   # Переопределение метода с учетом специфики класса
        return "Фью-фью!"                   # Вывод звука, характерного для птиц

    def fly(self):                          # Специфический метод - "летать"
        return f"{self.name} летит со скоростью {self.flight_speed} м/сек."

class Mammal(Animal):
    def __init__(self, name, age, has_fur):
        super().__init__(name, age)         # Вызов конструктора родительского класса
        self.has_fur = has_fur              # Специфический атрибут - "наличие шерсти"

    def make_sound(self):                   # Переопределение метода с учетом специфики класса
        return "Р-р-р!"                     # Вывод звука, характерного для млекопитающих

    def nurse(self):                        # Специфический метод - "вскармливание молоком"
        return f"{self.name} кормит детеныша молоком."

class Reptile(Animal):
    def __init__(self, name, age, is_venomous):
        super().__init__(name, age)         # Вызов конструктора родительского класса
        self.is_venomous = is_venomous      # Специфический атрибут - "ядовитость"

    def make_sound(self):                   # Переопределение метода с учетом специфики класса
        return "Шшш!"                       # Вывод звука, характерного для рептилий

    def slither(self):                      # Специфический метод - "ползать"
        return f"{self.name} ползет по земле."

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

def animal_sound(animals):
    for animal in animals:  # Перебор объектов в списке animals и вызов по каждому метода make_sound()
        print(f"{animal.name} говорит: {animal.make_sound()}")

# Создание объектов разных животных
sparrow = Bird("Воробей", 2, 0.5)
lion = Mammal("Лев", 5, True)
snake = Reptile("Змея", 3, True)

animals = [sparrow, lion, snake]    # Создание списка животных

animal_sound(animals)               # Вызов функции animal_sound