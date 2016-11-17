from questions.models import Location,Device,Question,Choice


class Modleiter(object):
    def __getitem__(self, item):
        if item >= len(self.things):
            raise IndexError("CustomRange index out of range")
        return self.things[item]

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
        self.location = Location.objects.get(locID)
        self.ansers = Choice.objects.filter(location=self.location)
        self.things = []
        for dev in self.location.devices:
            self.things.append(StatDevice(dev,self.ansers))



class StatDevice(Modleiter):
    def __init__(self,device,ansers):
        self.device = device
        self.questions = sef.device.questions
        Choobjects.filter(client=client_id).order_by('-check_in')

class Responce(Modleiter):
    def __init__(self,question,ansers):
