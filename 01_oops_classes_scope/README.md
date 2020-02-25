# Object Oriented Programming Day 1

### Learning Objectives
***Students Will Be Able To...***

* Initialize a class
* Call various methods from within a class
* Import a class

---
### Context

* Python is an object oriented language.
* It allows us to organize our code for efficiency and readability

---
### Lesson

#### Part 1 - What is OOP?

* Object Oriented Programming is the practice of writing your code around `Objects`
* This will become clearer as the lesson moves forward

#### Part 2 - What are Objects?

* Everything in Python is an object
* Every object is an `instance` of a class
* We know about the various data types and data structures. Well take `lists` for example. The moment you create a list you made an `instance` of it. This list now has access to all the methods inside the `list class` of Python3
* lists belong to a list class
* strings belong to a string class
* dictionaries belong to a dictionary class

#### Part 3 - Classes

* A class holds many methods that an object can respond to.
* They are defined with the word `class`
* They are always capitalized
* They are just blueprints for us to use later
* Lets make a class example for Car
* This car will take in three variables when created
* This car will have access to a method called `hello` that will print the make, model, and year to the to your terminal

```
class Car:
	"""
	We are making a car class
	"""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def hello(self):
		print("You have started your car, it is a {year} {make} {model}".format(year = self.year, make = self.make, model = self.model))

my_car = Car(make = "Bugatti", model = "Veyron", year = 2015)

my_car.hello()
```
* `docstring` - notice the three quotes followed by text and more three quotes?
	* This allows us to write multi line strings. 

***Five Min Exercise***

* Make a class of your favorite movie or tv show
* When the class is `instantiated` I want to have the following instance variables
	* self.cast
	* self.characters
	* self.release
	* self.genre
* I also want to be able to use the following methods
	* `.get_cast` will return me a list of cast members real names
	* `.get_characters` will return me a list of the characters in the movie
	* `.get_release` will return me the release date of that movie
	* `.get_genre` will return the genres this movie belongs to

#### Part 4 - Classes Terminology

* `Instantiate` - when we instantiate a class we are creating a new instance of that class.
* The`Car` class is a blueprint. We instantiate it by creating a variable with the Car class.
* This variable is now an `instance` of that care class
* We can use the class over and over again, if we had multiple cars, or in the example of your previous exercise, multiple movies.

#### Part 5 - Instance and Class Variables

* A class variable is a variable you want to be given to every instance of the class
* A instance variable is specific to that instance of the class
* The term `self` is used over and over again throughout class creation. This is referring to the object in that moment in time. (Instance of the object)
* Let's take the class example below

```
class Show:

    cinema = "Hollywood"
    
    def __init__(self, cast, characters, release, genre):
        self.cast = cast
        self.characters = characters
        self.release = release
        self.genre = genre

    def cast(self):
        return self.cast

    def char(self):
        return self.characters

    def date(self):
        return self.release

    def genre(self):
        return self.genre

p_cast = "Damian Lewis"
p_char = "Chuck Rhoades"

p_s_show = Show(p_cast , p_char , 2016, 'Drama')
top_gun = Show("Tom Cruise", "Maverick", 1986, "Action")
aos = Show("Chloe Bennett, Clark Gregg, Ming-Na Wen", "Skye, Coulson, May", 2013, "Comic")


print(p_s_show.cinema) === "Hollywood"
print(p_s_show.release()) === 2016

print(top_gun.cinema) === "Hollywood"
print(top_gun.release()) === 1986

print(aos.cinema) === "Hollywood"
print(aos.release()) === 2013
```
* `self` allows us to call the instance variables unique to that instance of a class
* We also specified a `class variable` with "cinema", that is a variable available to `EVERY INSTANCE OF THAT CLASS`

***Five Min Exercise***

* Create a class called `Athlete`
* Create three or more instances using that `Athelete` class
* Every athlete has two legs, two arms, and is_rich: (boolean variable set to true)
* Each athlete has THEIR OWN name, sport, team, height, weight

#### Part 6 - Instance, Class and Static Methods
 * Similar to variables, you also have instance methods. 
	* These are methods that you call on an instance of a class (object: Since an object is the instance of a class)
	* They have full access to the instance variables (state) of the object, which it accesses using the provided `self` variable

 * At the class level, we can also have class methods and static methods
	* These are defined with the decorator `@classmethod` and `@staticmethod`
	* These methods **do not** have access to the state of the object, since they are not associated with any particular instance. Instead they are associated to the class
	* The class and static methods can be invoked on the Class (ClassName.class_method(), or ClassName.static_method())
	* These methods are similar in that they do not affect the state of any object. They are used to perform stateless operations in a class.   

 * See Sample code	


#### Part 7 - Dunder Methods
Also known as `magic methods`. 

 * Start and end with double underscores
 * These are nothing more than methods within a class that can be called as expressions

```
class Area:

	def __init__(self, length, width):
		self.length = length
		self.width = width

	def calculate_area():
		return self.length * self.width

	def __str__(self):
		return "The Area is {}".format(self.score)

	def __add__(self, other_area):
		l = self.length + other_area.length
		w = self.width + other_area.width
		return Area(l, w)

rect1 = Area(5, 6)
rect2 = Area(2, 3)

# This will invoke the __add__() method which will "add" the two instances and return a third that represents addition
rect3 = rect1 + rect2

# This will invoke the __str__ method which returns a string representation of the instance 
print(rect1)		 
```

 * [Dunder Methods](https://www.python-course.eu/python3_magic_methods.php)

#### MISC

* triple quotes doc string used to comment your code and help others read your code
* If you want to try something else, check out Python Lambdas.
	* [Python Conquers the Universe Lambda Tutorial](https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/)
	* [Python 3 docs](https://docs.python.org/3/tutorial/controlflow.html)

#### Resources

* [Tutorials Point explanation of classes and objects](http://www.tutorialspoint.com/python/python_classes_objects.htm)