class Person(object):
    @classmethod
    def say(cls):
        return 'I\'m  a person';
print(Person.say())