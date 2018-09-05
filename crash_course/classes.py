# CLASSES & OBJECTS

class Person:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)

kobe = Person('Kobe Bryant', 'Kobebeef@outlook.com')
# kobe.set_name('Kobe Bryant')
# kobe.set_email('Kobebeef@outlook.com')

print(kobe.get_name())
print(kobe.toString())


class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(self.__name, self.__balance, self.__email)

hannibal = Customer('Hannibal Buress', 'handsomerambler@hotmail.com', 3000)
hannibal.set_balance(200)
print(hannibal.toString())

kate = Customer('Katie Holmes', 'katie@gmail.com', 67000)
print(kate.toString())
