class Dog:

	def __init__(self, name):
		self.name = name

	def speak(self):
		return "Guau!"


class Cat:
	
	def __init__(self, name):
		self.name = name

	def speak(self):
		return "Miau!"


def get_pet(pet="dog"):
	""" Factory method """

	pets = dict(dog=Dog("Goofy"), cat=Cat("Silvestre"))

	return pets[pet]


one_dog = get_pet("dog")
print(one_dog.speak())

one_cat = get_pet("cat")
print(one_cat.speak())
