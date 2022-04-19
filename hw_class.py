class Slim_Shady():
    """Описание класса: у артиста есть псевдоним и возраст.
    Класс: Slim_Shady
    Атрибуты объектов данного класса:
     - name
     - age
     методы объекта:
     - greeting()
     """
    """пункт б) - конструктор"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """пункт в) - greeting() является методом объекта класса Slim_Shady"""
    def greeting(self):
        print(f"""- Hi my name is...\n- What?\n- My name is...\n- Who?\n- My name is...\n- It is {self.name}\n""")


"""пункт г) - создаём объект person класса Slim_Shady"""
singer = Slim_Shady('Eminem', 49)

"""пункт д) - выводим атрибуты объекта на экран"""
print(singer.name, singer.age)

"""пункт e) - обращаемся к методу объекта"""
singer.greeting()

