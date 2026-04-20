class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, высшего образования {education}")


human1 = Person('Крисс', '16 июня', 'учитель', True)
human2 = Person('Роб', '1 августа', 'студент', False)
human3 = Person('Том', '25 мая', 'дизайнер', True)
print(human1.name, human1.birth_date, human1.occupation, human1.higher_education)
print(human2.name, human2.birth_date, human2.occupation, human2.higher_education)
print(human3.name, human3.birth_date, human3.occupation, human3.higher_education)

human1.introduce()
human2.introduce()
human3.introduce()