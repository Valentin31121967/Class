import json
class User:
# Создаем конструктор класса User
    def _init_(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.age = None
# Вводим исходные данные пользователя
    def input_fio(self):
        self.first_name = input("Input First Name: ")
        self.middle_name = input("Input Middle Name: ")
        self.last_name = input("Input Last Name: ")
    def input_age(self):
        self.age = input("Input Age: ")
# Создаем удобную для вывода на экран строку пользователя
    def serialize(self):
        return "First name: {}\n" \
               "Middle name: {}\n"\
               "Last name: {}\n" \
               "Age : {}\n"\
            .format(self.first_name, self.middle_name, self.last_name, self.age)
# Сохраняем данные в файл с помощью json
    def fail_save(self):
        fil = str(input("Введите с клавиатуры имя файла для записи на диск:  "))
        jdata = json.dumps((self.first_name, self.middle_name, self.last_name, self.age))
        with open(fil, "w") as f:
            f.write(jdata)
# Загружаем с файла данные для работы
    def fail_load(self):
        fil = str(input("Введите с клавиатуры имя файла для загрузки с диска:  "))
        with open(fil, "r") as f:
            d = f.read()
            p = json.loads(d)
        print(type(p))
        print(p)
# Вызываем все необходимые методы для работы  кода программы
chelovek = User()
chelovek.input_fio()
chelovek.input_age()
print(chelovek.serialize())
print(type(chelovek.serialize()))
print(chelovek)
print(type(chelovek))
chelovek.fail_save()
print(chelovek.fail_load())