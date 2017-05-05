class Person(object):
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email = email

    def tanzen(self):
        print "Seht her ich heisse", self.first_name, "ich kann super gut tanzen"

albert = Person('Albert','Zopf','0664-985348',1990,'albert@email.com')
albert.tanzen()