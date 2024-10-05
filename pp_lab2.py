# Клас Фільм
class Film:
    # Атрибут класу (наприклад, курс долара)
    exchange_rate = 1.0  # Статичний атрибут класу

    # Конструктор з параметрами
    def __init__(self, title="Невідомий фільм", director="Невідомий режисер", duration=0, num_actors=0):
        self._title = title  # Приватний атрибут
        self._director = director
        self.duration = duration
        self.num_actors = num_actors

    # Властивість для назви фільму
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(value) > 0:
            self._title = value

    # Метод для розрахунку вартості
    def cost(self):
        cost = self.duration * 20 + self.num_actors * 30
        if self._director in ["Стівен Спілберг", "Джеймс Кемерон"]:
            cost *= 2
        return cost * Film.exchange_rate  # Використовуємо статичний атрибут

    # Метод __str__ для строкового подання
    def __str__(self):
        return f"Фільм: {self.title}, Режисер: {self._director}, Тривалість: {self.duration} хв., Акторів: {self.num_actors}"

    # Статичний метод
    @staticmethod
    def set_exchange_rate(rate):
        Film.exchange_rate = rate

    # Декоратор методу для демонстрації
    def show_decorator(func):
        def wrapper(*args, **kwargs):
            print("Метод викликається")
            result = func(*args, **kwargs)
            print("Метод завершився")
            return result
        return wrapper

# Клас Мультфільм (наслідується від Фільм)
class Cartoon(Film):
    # Перевизначаємо метод cost для мультфільму
    def cost(self):
        return self.duration * 25 + self.num_actors * 10

# Додаткові класи для БД
class DatabaseEntity:
    def __init__(self, name="Невідоме ім'я", age=0):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value

    def save_to_db(self):
        print(f"Збережено {self._name} до бази даних")

# Другий батьківський клас для множинного наслідування
class Animal:
    def __init__(self, is_happy=True):
        self.is_happy = is_happy

    def make_sound(self):
        return "Some generic sound"

# Дочірній клас з множинним наслідуванням
class Dog(DatabaseEntity, Animal):
    def __init__(self, name, age, is_happy):
        DatabaseEntity.__init__(self, name, age)
        Animal.__init__(self, is_happy)

    def bark(self):
        return "Woof! Woof!"

    def save_to_db(self):
        super().save_to_db()
        print(f"Збережено {self._name} як собаку")

# Демонстраційна програма
def demo():
    # Створюємо екземпляр класу Фільм
    film = Film("Jurassic Park", "Стівен Спілберг", 127, 15)
    print(film)
    print(f"Вартість фільму: {film.cost()} тис. доларів")

    # Створюємо екземпляр класу Мультфільм
    cartoon = Cartoon("Toy Story", "Джон Лассетер", 81, 8)
    print(cartoon)
    print(f"Вартість мультфільму: {cartoon.cost()} тис. доларів")

    # Створюємо екземпляр класу Dog (множинне наслідування)
    dog = Dog("Buddy", 3, True)
    print(dog.bark())
    dog.save_to_db()

demo()