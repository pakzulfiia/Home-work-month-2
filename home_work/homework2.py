class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
    
    def introduce(self):
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я одноклассник Тимура, родился {self.birth_date}, работаю {self.occupation}')

class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я друг Алмаза, родился {self.birth_date}, работаю {self.occupation}')

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f'мы дружим со {self.shared_memory}')
    

person1 = Person('Рафаэль', '11.04.1999', 'учитель')
person1.introduce()

student1 = Classmate('Алмаз', '05.03.2003', 'программистом', 'PP21')
student2 = Classmate('kate', '05.03.2003', 'программистом','bg65-1')
student1.introduce()
print(student1.group_name)

human1 = Friend('Тимур', '05.06.2000', 'дизайнером', 'карточные игры')
human2 = Friend('Коля', '05.06.2000', 'дизайнером', 'гольф')
human1.introduce()
print(human1.hobby)
print()
bestie = BestFriend('Коля', '05.06.2000', 'дизайнером', 'гольф', 'школьных лет')
bestie.introduce()
print()
they_all = [person1, student1, human1]
for h in they_all:
    h.introduce()