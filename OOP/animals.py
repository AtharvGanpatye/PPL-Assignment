
from abc import ABC, abstractmethod

##########################################################################################
class Bird:
	def __init__(self, species, sub_species = None):
		self.__class = "Aves"
		self.__species = species
		self.__subspecies = None
		self.__flying = None
		self.__color = None
		self.__size = None
		self.__beak = None
		self.__special = None
		self.__sound = None

	def set_flying(self, b):
		self.__flying = b

	def is_flying(self):
		return self.__flying

	def get_speciality(self):
		print("Speciality of {}:\n  Color : {}.\t Size : {}.\t Beak : {}. \t {}".format(self.__species, self.__color, self.__size, self.__beak, self.__special))

	def set_speciality(self, color, size, beak, special = None):
		self.__color = color
		self.__size = size
		self.__beak = beak
		self.__special = special

	def set_sound(self, sound):
		self.__sound = sound

	def get_sound(self):
		print("Sound of {} is {}".format(self.__species, self.__sound))

##########################################################################################

class Eagle(Bird):

	def __init__(self, sub_species):
		super().__init__("Eagle", sub_species)
		self.__wingspan = None
		self.set_sound("Kleek Kleek")

	def set_wingspan(self, w):
		self.__wingspan = w

	def get_wingspan(self):
		print("Wingspan is {} meters.".format(Self.__wingspan))

##########################################################################################

class Peacock(Bird):

	def __init__(self):
		super().__init__("Peacock")
		self.set_sound("Meow")
		self.__plumage = None

	def set_plumage(self, val):
		self.__plumage = val

	def is_plumage_spread(self, val):
		return self.__plumage

##########################################################################################

class Elephant(ABC):

	@abstractmethod
	def __init__(self, gender, age):
		self._gender = gender
		self._age = age
		self.__tusks = None

	@abstractmethod
	def set_ears(self, ears):
		self.__ears = ears

	def set_tusks(self, b):
		self.__tusks = b

	def get_tusks(self):
		return self.__tusks

	def set_species(self, species):
		self._species = species
	
	def get_speciality(self):
		pass

##########################################################################################

class Asian_Elephant(Elephant):

	def __init__(self, gender, age):
		super().__init__(gender, age)
		super().set_species("Asian Elephant")
		self.__size = "Smaller than African Elephants"
		self.__weight = None

	def set_ears(self, ears):
		self.__ears = ears

	def set_weight(self, w = None):
		self.__weight = w

	def get_weight(self, w = None):
		print("Weight : {} kg".format(self.__weight))

	def get_speciality(self):
		print("Speciality of {}:\n  Ears : {}. \tSize: {}.".format(self._species, self.__ears, self.__size))

	def describe(self):
		print("{}\t {} yrs\n {}\t {} kg".format(self._species, self._age, self._gender, self.__weight))

##########################################################################################

class African_Elephant(Elephant):

	def __init__(self, gender, age):
		super().__init__(gender, age)
		super().set_species("African Elephant")
		self.__size = "Larger than Asian Elephants"
		self.__weight = None

	def set_ears(self, ears):
		self.__ears = ears

	def set_weight(self, w = None):
		self.__weight = w

	def get_weight(self, w = None):
		print("Weight : {} kg".format(self.__weight))

	def get_speciality(self):
		print("Speciality of {}:\n  Ears : {}. \tSize: {}.".format(self._species, self.__ears, self.__size))

	def describe(self):
		print("{}\t {} yrs\n{}\t {} kg".format(self._species, self._age, self._gender, self.__weight))

##########################################################################################

class Dog:
    
    def __init__(self, name, age):
        self.Class = 'Mammal'
        self.__name = name
        self.__age = age
        self.__breed = None
        self.__color = None
        self.__voice = 'Barks'
        self.__running = None
        self._tail = None
        self._height = None
        self._skin = None

    def get_sound(self):
        print("Dog {}.".format(self.__voice))

    def set_breed(self, breed):
        self.__breed = breed

    def get_breed(self):
        print("Breed of dog is : {}.".format(self.__breed))

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        print("Color of Dog is : {}.".format(self.__color))

    def set_speciality(self, tail, height, skin):
        self._tail = tail
        self._height = height
        self._skin = skin

    def running(self, boolean):
        self.__running = boolean

    def is_running(self):
        return self.__running

    def describe(self):
        print("Species : {}\nAnimal : Dog\tBreed : {}\nName : {}\tAge : {} yrs".format(self.Class, self.__breed, self.__name, self.__age))

##########################################################################################

class Labrador(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.set_breed("Labrador")
        super().set_speciality("Long Hairy Tail", "Medium Height", "Hairy Skin")

    def get_speciality(self):
        print("Speciality of Labrador breed :\n {} \t {} \t {}".format(self._height, self._tail, self._skin))


class Doberman(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.set_breed("Doberman")
        super().set_speciality("Short Tail", "Tall Height", "Less fur")

    def get_speciality(self):
        print("Speciality of Doberman breed :\n {} \t {} \t {}".format(self._height, self._tail, self._skin))



class Pug(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.set_breed("Pug")
        super().set_speciality("Short Tail", "Short Height", "Moderate fur")

    def get_speciality(self):
        print("Speciality of Pug breed :\n {} \t {} \t {}".format(self._height, self._tail, self._skin))

##########################################################################################

if __name__ == '__main__':
	
	b1 = Eagle("Bald Eagle")
	b1.set_flying(True)
	b1.set_sound("Kleek")
	b1.set_speciality("Dark Brown", "Large", "Curved Yellow Beak", "White Neck")
	b1.get_speciality()
	print("\n")

	p1 = Peacock()
	p1.set_sound("Meow")
	p1.set_speciality("Blue", "Large", "Small Beak", "Beautiful Plumage")
	p1.get_speciality()
	p1.set_plumage(True)
	print("\n")

	e1 = Asian_Elephant("Female", 5)
	e1.set_ears("Smaller Ears")
	e1.set_tusks(False)
	e1.set_weight(5500)
	e1.describe()
	e1.get_speciality()
	print("\n")

	e2 = African_Elephant("Male", 3)
	e2.set_ears("Larger Ears")
	e2.set_tusks(True)
	e2.set_weight(8000)
	e2.describe()
	e2.get_speciality()
	print("\n")

	d1 = Dog("Tommy", 3)
	d1.set_color('Brown-White')
	d1.describe()
	print("\n")

	l = Labrador("Jimmy", 4)
	l.set_color("Brown-White")
	l.describe()
	l.get_speciality()
	print("\n")

	d = Doberman("Mike", 3.5)
	d.describe()
	d.get_speciality()
	print("\n")

	p = Pug("Leo", 2)
	p.set_color("White")
	p.describe()
	p.get_speciality()
	print("\n")
