from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education = False):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education
    
    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education
    
    @property
    def birth_date(self):
        return self.__birth_date
    
    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y").date()
        today = datetime.today()
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    def introduce(self):
        education = "есть" if self.__higher_education else "нет"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, высшее образование {education}")

class Classmate(Person):
    def __init__(self, name, birth_date, group_name, occupation, higher_education = False):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(f'Привет, меня зовут {self.name}, я одноклассник Тимура, мы учимся в группе {self.group_name}. Я родился {self.birth_date}, работаю {self.occupation}, высшее образование {education}')

class Friend(Person):
    def __init__(self, name, birth_date, hobby, occupation, higher_education = False):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(f'Привет, меня зовут {self.name}, я друг Алмаза, родился {self.birth_date}, мое хобби {self.hobby}. Я работаю {self.occupation}, высшее образование {education}')

person1 = Person('Рафаэль', '11.04.1999', 'учитель')
person1.introduce()
print('возраст:', person1.age)
human1 = Friend('Коля', '05.06.2000', 'гольф', 'дизайнером', False)
human1.introduce()
print('возраст:', human1.age)
student1 = Classmate('Алмаз', '05.03.2003', 'PP21', 'программистом', True)
student1.introduce()
print('возраст:', student1.age)