# Object Oriented Programming Day 2

### Learning Objectives
***Students Will Be Able To...***

* Utilize classes using Inheritance
* Use items from a parent class
* Use items from a child class
* Utilize the terminal to help research

---
### Lesson

#### Part 1 - OOP 5 min recap

* Yesterday we were introduced to the idea that everything in Python is an Object
* We wrote classes
* Instance Variables vs Instance methods
* Scope - LEGB

#### Part 2 - Inheritance

 * Allows you to create `derived` classes, that `inherit` code from another pre-defined class
 * The inheriting class is called a `sub-class` or `child-class`, the class being inherited from is the `parent class` or `base class`.
 * The sub class will inherit all of the methods and attributes of the base class
 * The inherited methods and attributes can be `overridden`: The child class may choose to redefine an inherited method which will take precedence over the inherited code
    * Think of inheritence as an attempt to model `specialization` in the real world. 
    * As you go from Parent to Children classes you go from general to specific / concrete. 
    * eg. Vehicle -> Car -> Suv  or Vehicle -> Bike -> Mountain Bike   `IS-A` relationship
    * See: Sample Code
 * The sub-class can also have methods of it's own in addition to the inherited code
    * eg. The class Bike will have a method `pedal` which doesn't exist in the parent Vehicle class
 * Python supports Multiple Inheritence
    * You do this by specifying multiple base classes in the class definition
    * Can lead to complex code
 
##### Abstract Classes

 * Base classes can be set as `abstract` but do not want to allow instances of these classes to get created
 * Used to force uniformity in sub-classes by having them adhere to the interface of the base abstract class. 
 * Used to model Abstract concepts in the real world
 * eg. The Vehicle Base class could be defined as Abstract
    * The drive method could have been set as abstract as well which would force all sub-classes to override and implement it
 * Done using the `abc` module: `from abc import ABC, abstractmethod`   

##### Exercise 
* Make a class Pet
* Make a class Dog
* Make a class Cat
* Make a class Bird

```
class Pet:
    eyes = 2
    legs = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("You got a new pet")

    def jump(self):
        print("your pet is jumping")

class Dog(Pet):

    def __init__(self, name, age, breed):
        Pet.__init__(self, name, age)
        self.breed = breed

    def speak(self):
        print("Bark Bark")

class Cat(Pet):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")

shadow = Dog(name = "Shadow", age = 17, breed = "Labrador")

lucy = Cat(name = "Lucy", age = 13)

shadow.eyes
lucy.legs
shadow.speak()
lucy.speak()

```
* The local method takes precedent over the parent method
* If all pets have a name and an age we can put it in the parents `init` method
    * To utilize the parent `init` method we could call it inside of the child's `init` method and pass the values through to the parent

***NOTE***

* In the above example, class Pet can be written like so:

```
class Pet(object):
```
* You may be familiar with this syntax if you did tutorials in python 2
* What this means is that `ALL` classes will be inheriting from the `Object` class

***Five Min Exercise***

* Make a parent class called `Vehicle`
* Make three child classes: `Car`, `Truck`, `Motorcycle`
* Instantiate the child classes
* Each child should have their own unique methods that will return an instance variable
* Each child should also have access to variables inside of the parent class

#### Part 3 - Best Practices

***Pseudo Code***

* Before writing any real code just make bullets of what is your goal, what is your endpoint, and how can you get there
* Plan out your app, what classes will you have, what methods will be inside of those classes

#### Other best practices
 
* Inside your terminal make use of 
	* help()
	* dir()
	* doc_strings = """ This Is A Doc String """
	* Open a file inside Python REPL using `-i`
		* `python3 -i my_file.py`

#### More complicated OOP concepts to checkout
 
 * Class methods vs. Static methods
 	* [Python Methods and How They Work](https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods)

```
class Blah:
	
```	
 
 * Look at the following code:
 
```
 class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super().__init__()

ChildA()
ChildB()
```
* What's the difference? Research here: 
	* [http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods](http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods)
* `Class.__init__` vs. `def __init__` vs. super
	* [http://learnpythonthehardway.org/book/ex44.html](http://learnpythonthehardway.org/book/ex44.html)
    * [http://stackoverflow.com/questions/1173992/what-is-a-basic-example-of-single-inheritance-using-the-super-keyword-in-pytho](http://stackoverflow.com/questions/1173992/what-is-a-basic-example-of-single-inheritance-using-the-super-keyword-in-pytho)
- Checkout this usage of Super --> [http://i.imgur.com/SOniuXb.png](http://i.imgur.com/SOniuXb.png)
	