'''
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
'''

class Worker:

    def __init__(self, n='Ivan', s='Vasilev', p='designer', w=100, b=50):
        self.name = n
        self.surname = s
        self.position = p
        self.wage = w
        self.bonus = b
        self._income = {"wage": self.wage, "bonus": self.bonus}

class Position(Worker):
    def get_full_name (self):
        return self.name + ' ' + self.surname

    def get_total_income (self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f'{self.name} {self.surname} - {self._income["wage"] + self._income["bonus"]}'

if __name__ == '__main__':
    pos_inf = Position('Vasya', 'Ivanov', 'designer', 350, 50)
    print(pos_inf.get_full_name())
    print(pos_inf.get_total_income())
    print(pos_inf)


