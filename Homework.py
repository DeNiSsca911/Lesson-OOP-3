# Базовый класс для всех животных
class Animal:
    # Конструктор класса Animal
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age  # Возраст животного

    # Метод для издания звука (будет переопределен в дочерних классах)
    def make_sound(self):
        pass

    # Метод для кормления животного
    def eat(self):
        print(f"{self.name} кушает.")

# Класс птиц, наследуется от Animal
class Bird(Animal):
    # Конструктор класса Bird
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.wingspan = wingspan  # Размах крыльев птицы

    # Переопределение метода издания звука для птиц
    def make_sound(self):
        print(f"{self.name} говорит: Чик-чирик!")


# Класс млекопитающих, наследуется от Animal
class Mammal(Animal):
    # Конструктор класса Mammal
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.fur_color = fur_color  # Цвет шерсти млекопитающего

    # Переопределение метода издания звука для млекопитающих
    def make_sound(self):
        print(f"{self.name} говорит: Ррррр!")


# Класс рептилий, наследуется от Animal
class Reptile(Animal):
    # Конструктор класса Reptile
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.scale_type = scale_type  # Тип чешуи рептилии

    # Переопределение метода издания звука для рептилий
    def make_sound(self):
        print(f"{self.name} говорит: Шшшшш!")


# Функция для демонстрации полиморфизма - издает звуки всех животных
def animal_sound(animals):
    for animal in animals:  # Перебираем всех животных в списке
        animal.make_sound()  # Вызываем метод make_sound() для каждого животного


# Класс смотрителя зоопарка
class ZooKeeper:
    # Конструктор класса ZooKeeper
    def __init__(self, name):
        self.name = name  # Имя смотрителя

    # Метод для кормления животного
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


# Класс ветеринара
class Veterinarian:
    # Конструктор класса Veterinarian
    def __init__(self, name):
        self.name = name  # Имя ветеринара

    # Метод для лечения животного
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


# Класс зоопарка (использует композицию для хранения животных и сотрудников)
class Zoo:
    # Конструктор класса Zoo
    def __init__(self):
        self.animals = []  # Список животных в зоопарке
        self.staff = []  # Список сотрудников зоопарка

    # Метод для добавления животного в зоопарк
    def add_animal(self, animal):
        self.animals.append(animal)  # Добавляем животное в список
        print(f"Добавлен {animal.__class__.__name__} {animal.name} в зоопарк")

    # Метод для добавления сотрудника в зоопарк
    def add_staff(self, staff_member):
        self.staff.append(staff_member)  # Добавляем сотрудника в список
        print(f"Добавлен сотрудник {staff_member.__class__.__name__} {staff_member.name} в зоопарк")

    # Метод для сохранения состояния зоопарка в файл
    def save_zoo(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:  # Открываем файл для записи
            # Сохраняем информацию о животных
            f.write("Животные:\n")
            for animal in self.animals:
                # Записываем тип, имя и возраст каждого животного
                f.write(f"{animal.__class__.__name__},{animal.name},{animal.age}\n")

            # Сохраняем информацию о сотрудниках
            f.write("\nСотрудники:\n")
            for staff in self.staff:
                # Записываем должность и имя каждого сотрудника
                f.write(f"{staff.__class__.__name__},{staff.name}\n")
        print(f"Состояние зоопарка сохранено в {filename}")

    # Метод для загрузки состояния зоопарка из файла
    def load_zoo(self, filename):
        self.animals = []  # Очищаем список животных
        self.staff = []  # Очищаем список сотрудников

        with open(filename, 'r', encoding='utf-8') as f:  # Открываем файл для чтения
            section = None  # Переменная для определения текущей секции файла
            for line in f:
                line = line.strip()  # Удаляем лишние пробелы
                if not line:  # Пропускаем пустые строки
                    continue

                # Определяем текущую секцию
                if line == "Животные:":
                    section = "animals"
                    continue
                elif line == "Сотрудники:":
                    section = "staff"
                    continue

                # Обрабатываем секцию с животными
                if section == "animals":
                    animal_type, name, age = line.split(',')  # Разбиваем строку на части
                    age = int(age)  # Преобразуем возраст в число

                    # Создаем объект животного в зависимости от типа
                    if animal_type == "Bird":
                        animal = Bird(name, age, 0)
                    elif animal_type == "Mammal":
                        animal = Mammal(name, age, "")
                    elif animal_type == "Reptile":
                        animal = Reptile(name, age, "")

                    self.animals.append(animal)  # Добавляем животное в список

                # Обрабатываем секцию с сотрудниками
                elif section == "staff":
                    staff_type, name = line.split(',')  # Разбиваем строку на части

                    # Создаем объект сотрудника в зависимости от типа
                    if staff_type == "ZooKeeper":
                        staff = ZooKeeper(name)
                    elif staff_type == "Veterinarian":
                        staff = Veterinarian(name)

                    self.staff.append(staff)  # Добавляем сотрудника в список

        print(f"Состояние зоопарка загружено из {filename}")


# Основной блок программы
if __name__ == "__main__":
    # Создаем зоопарк
    my_zoo = Zoo()

    # Создаем животных
    parrot = Bird("Кеша", 2, 15)  # Попугай
    lion = Mammal("Симба", 5, "золотистый")  # Лев
    snake = Reptile("Каа", 3, "гладкая")  # Змея

    # Создаем сотрудников
    keeper = ZooKeeper("Иван")  # Смотритель
    vet = Veterinarian("Мария")  # Ветеринар

    # Добавляем животных и сотрудников в зоопарк
    my_zoo.add_animal(parrot)
    my_zoo.add_animal(lion)
    my_zoo.add_animal(snake)
    my_zoo.add_staff(keeper)
    my_zoo.add_staff(vet)

    # Демонстрируем полиморфизм - разные животные издают разные звуки
    print("\nЗвуки животных:")
    animal_sound(my_zoo.animals)

    # Демонстрируем работу сотрудников
    print("\nДействия сотрудников:")
    keeper.feed_animal(parrot)  # Смотритель кормит попугая
    vet.heal_animal(lion)  # Ветеринар лечит льва

    # Сохраняем состояние зоопарка в файл
    my_zoo.save_zoo("мой_зоопарк.txt")

    # Создаем новый зоопарк и загружаем состояние из файла
    new_zoo = Zoo()
    new_zoo.load_zoo("мой_зоопарк.txt")

    # Демонстрируем загруженных животных
    print("\nЗагруженные животные:")
    animal_sound(new_zoo.animals)