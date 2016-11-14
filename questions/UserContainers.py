from questions.models import Location

class UserFactory(object):

	def __init__(self,supervisor=None):
		if supervisor:
			self.locations = Location.objects.filter(admin=supervisor)
		else:
			self.locations = Location.objects.all()
		self.names = set([loc.user_assigned for loc in self.locations])
		self.users = []
		for name in self.names:
			self.users.append(User(name))

	def __iter__(self):
		return self.users

class User(object):
	def __init__(self,name):
		self.name=name
		self.locations = Location.objects.filter(user_assigned=name)
	def __iter__(self):
		return self.locations
