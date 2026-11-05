# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

        if (type(name) is not str) or (type(birth) is not date):
            raise TypeError
        
        if len(name) == 0:
            raise ValueError


    def initials(self):
        seperated = self.name.split()

        answer = ""
        for word in seperated:
            answer += word[0].upper()
        
        return answer
    
    def is_birthday(self):
        today = date.today()
        return (self.birth.month == today.month) and (self.birth.day == today.day)

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

per = Person("", date(2007, 11, 5))
print(per.initials())
print(per.is_birthday())