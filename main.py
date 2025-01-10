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
parrot = Bird("Попугай", 2, 0.25)
lion = Mammal("Лев", 5, True)
snake = Reptile("Змея", 3, True)

animals = [sparrow, parrot, lion, snake]    # Создание списка животных

# Для объекта parrot переопределим метод make_sound
parrot.make_sound = lambda: "Попка-дурак"  # Переопределяем только для объекта parrot

animal_sound(animals)                       # Вызов функции animal_sound

# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

class Employee:
    def __init__(self, name, gender, age):
        self.name = name      # Имя сотрудника
        self.gender = gender  # Пол сотрудника
        self.age = age        # Возраст сотрудника
        self.position = None  # Должность, по умолчанию не определена

    def __str__(self):        # Строковое представление информации о сотруднике
        return f"{self.name}, {self.gender}, {self.age} лет, Должность: {self.position if self.position else 'Не определена'}"

    def work(self):                 # Метод, отражающий факт работы в зоопарке
        return f"{self.name} работает в зоопарке."

    def take_break(self):           # Метод перерыва на обед
        return f"{self.name} берет перерыв."

    def get_info(self):             # Получение информации о сотруднике
        return f"Сотрудник: {self.name}, Пол: {self.gender}, Возраст: {self.age} лет, Должность: {self.position if self.position else 'Не определена'}"

    def assign_position(self, position):
        self.position = position    # Присвоение должности сотруднику

class Zoo:
    def __init__(self):
        self.animals = []     # Список животных в зоопарке
        self.employees = []   # Список сотрудников зоопарка

    def add_animal(self, animal):
        self.animals.append(animal)      # Добавление животного в зоопарк

    def add_employee(self, employee):
        self.employees.append(employee)  # Добавление сотрудника в зоопарк

    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.__class__.__name__})")

    def show_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee}")

# Создание объектов животных
parrot = Bird("Попугай", 2, 0.25)
lion = Mammal("Лев", 5, True)
snake = Reptile("Змея", 3, True)

# Создание сотрудников
employee1 = Employee("Петров И.С.", "пол: муж.", "55")      # Без должности
employee2 = Employee("Сидорова М.А.", "пол: жен.", "35")    # Без должности

# Создание зоопарка, как конкретного объекта
zoo = Zoo()

# Добавление животных и сотрудников в зоопарк
zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

zoo.add_employee(employee1)
zoo.add_employee(employee2)

# Вывод информации о животных и сотрудниках
zoo.show_animals()
zoo.show_employees()

# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).

# Класс ZooKeeper (Смотритель зоопарка) - наследуется от Employee
class ZooKeeper(Employee):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.assign_position("Смотритель зоопарка")  # Присвоение должности

    def feed_animal(self, animal):
        # Смотритель кормит животное
        return f"{self.name} кормит {animal.name}."

# Класс Veterinarian (Ветеринар) - наследуется от Employee
class Veterinarian(Employee):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.assign_position("Ветеринар")  # Присваиваем должность
    def heal_animal(self, animal):
        # Ветеринар лечит животное
        return f"{self.name} лечит {animal.name}."

employee2.assign_position("Смотритель зоопарка")
employee1.assign_position("Ветеринар")

print(employee1.get_info())
print(employee2.get_info())