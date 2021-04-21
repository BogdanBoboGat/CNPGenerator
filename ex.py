#!/usr/bin/python3
import names
import random

class human():
    def __init__(self):
        
        self.day = random.randrange(1, 31)
        self.month = random.randrange(1, 12)
        self.year = random.choice([random.randrange(50, 99), random.randrange(0, 21)])
        
        sex = random.choice([1, 2, 3, 4, 5, 6])
        other = random.randrange(99999, 999999)

        if sex % 2 == 0:
            self.sex = 'female'
            self.name = names.get_full_name(gender='female')
        else:
            self.sex = 'male'
            self.name = names.get_full_name(gender='male')

        if self.day < 10:
            
            if self.month < 10:
                
                if self.year < 10:
                    self.cnp = str(sex) + '0' + str(self.year) + '0' + str(self.month) + '0' + str(self.day) + str(other)
        
                else:
                    self.cnp = str(sex) + str(self.year) + '0' + str(self.month) + '0' + str(self.day) + str(other)

            else:

                if self.year < 10:
                    self.cnp = str(sex) + '0' + str(self.year) + str(self.month) + '0' + str(self.day) + str(other)
        
                else:
                    self.cnp = str(sex) + str(self.year) + str(self.month) + '0' + str(self.day) + str(other)
        
        else:
            if self.month < 10:
                
                if self.year < 10:
                    self.cnp = str(sex) + '0' + str(self.year) + '0' + str(self.month)  + str(self.day) + str(other)
        
                else:
                    self.cnp = str(sex) + str(self.year) + '0' + str(self.month) + str(self.day) + str(other)

            else:

                if self.year < 10:
                    self.cnp = str(sex) + '0' + str(self.year) + str(self.month) + str(self.day) + str(other)
        
                else:
                    self.cnp = str(sex) + str(self.year) + str(self.month) + str(self.day) + str(other)


    def __str__(self):
        if self.day < 10:
            
            if self.month < 10:
                
                if self.year < 10:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in 0{self.day}.0{self.month}.200{self.year} and my Romanian CNP is {self.cnp}.'
        
                elif self.year > 10 and self.year < 22:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in 0{self.day}.0{self.month}.20{self.year} and my Romanian CNP is {self.cnp}.'
        
                else:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in 0{self.day}.0{self.month}.19{self.year} and my Romanian CNP is {self.cnp}.'

            else:

                if self.year < 10:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in 0{self.day}.{self.month}.200{self.year} and my Romanian CNP is {self.cnp}.'
        
                elif self.year > 10 and self.year < 22:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in 0{self.day}.{self.month}.20{self.year} and my Romanian CNP is {self.cnp}.'
        
                else:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in 0{self.day}.{self.month}.19{self.year} and my Romanian CNP is {self.cnp}.'
        
        else:
            if self.month < 10:
                
                if self.year < 10:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in {self.day}.0{self.month}.200{self.year} and my Romanian CNP is {self.cnp}.'
        
                elif self.year > 10 and self.year < 22:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in {self.day}.0{self.month}.20{self.year} and my Romanian CNP is {self.cnp}.'
        
                else:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in {self.day}.0{self.month}.19{self.year} and my Romanian CNP is {self.cnp}.'

            else:

                if self.year < 10:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in {self.day}.{self.month}.200{self.year} and my Romanian CNP is {self.cnp}.'
        
                elif self.year > 10 and self.year < 22:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in {self.day}.{self.month}.20{self.year} and my Romanian CNP is {self.cnp}.'
        
                else:
                    return f'Hello! My name is {self.name}, I am a {self.sex}. I was born in {self.day}.{self.month}.19{self.year} and my Romanian CNP is {self.cnp}.'

for i in range(10):
    print(human())
