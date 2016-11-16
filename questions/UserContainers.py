from questions.models import Location

class UserFactory(object):

    def __init__(self,supervisor=None):
        self.meow = 0
        self.locations = Location.objects.all()
        print(self.locations)
        self.names = set([loc.user_assigned for loc in self.locations])
        self.names.sort()
        self.users = []
        for name in sorted(self.names):
        	self.users.append(User(name))
    def __getitem__(self, item):
        if item >= len(self.users):
            raise IndexError("CustomRange index out of range")
        return self.users[item]

    def __len__(self):
        return len(self.users)



class User(object):
    def __init__(self,name):
        self.name=name
        self.locations = Location.objects.filter(user_assigned=name)
    def __getitem__(self, item):
        if item >= len(self.locations):
            raise IndexError("CustomRange index out of range")
        return self.locations[item]

    def __len__(self):
        return len(self.locations)
