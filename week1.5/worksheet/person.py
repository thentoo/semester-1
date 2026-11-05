# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a person with the given name and date of birth.

        Raises TypeError if name is not a str or birth is not a date.
        Raises ValueError if name is empty.
        """
        self.name = name
        self.birth = birth

        if (type(name) is not str) or (type(birth) is not date):
            raise TypeError

        if len(name) == 0:
            raise ValueError


    def initials(self):
        """
        Returns the initials of this person's name (first letter of each word, upper case).
        """
        seperated = self.name.split()

        answer = ""
        for word in seperated:
            answer += word[0].upper()

        return answer


    def is_birthday(self):
        """
        Returns True if today is this person's birthday, otherwise False.
        """
        today = date.today()
        return (self.birth.month == today.month) and (self.birth.day == today.day)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

per = Person("", date(2007, 11, 5))
print(per.initials())
print(per.is_birthday())