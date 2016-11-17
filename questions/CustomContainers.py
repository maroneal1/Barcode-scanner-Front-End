from questions.models import Location


class Modleiter(object):
    def __getitem__(self, item):
        if item >= len(self.things):
            raise IndexError("CustomRange index out of range")
        return self.users[things]

    def __len__(self):
        return len(self.things)

class UserFactory(Modleiter):
    def __init__(self,supervisor=None):
        self.meow = 0
        self.locations = Location.objects.all()
        print(self.locations)
        self.names = set([loc.user_assigned for loc in self.locations])
        self.things = []
        for name in sorted(self.names):
        	self.things.append(User(name))


class User(Modleiter):
    def __init__(self,name):
        self.name=name
        self.things = Location.objects.filter(user_assigned=name)



class StatDeviceFactory(Modleiter):
    def __init__(self,locID):

        self.things = Location.objects.filter(user_assigned=name)

class StatDevice(Modleiter):
    def __ini__(self,devID):
        pass
