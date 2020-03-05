class Fizz:
    ''' The fizz value of n = "fizz" if n is evenly divisible by 3. If n is not divisible by 3 then the fizz value is the value of n converted into a string.'''

    def __init__(self, start = 0):
        self.number = start
    
    def next(self):
        #This method increases the value of number by 1 and then returns a string of that number's fizz value.
        self.number = self.number + 1
        if (self.number % 3) == 0:
            return "fizz"
        else:
            return str(self.number) 
        return 

buzzer = Fizz(11)
assert buzzer.next() == "fizz"
assert buzzer.next() == "13"
assert buzzer.next() == "14"


class Buzz(Fizz):
    '''
    It should have a constructor like Fizz where it takes in an argument start with a default value of 0 but it should not have any instance variable of its own. Instead it should rely on the inherited class Fizz's number value (which will require you to invoke the constructor of the base class Fizz from Buzz's constructor).

    Buzz should have a method next which should return the next buzz value. The buzz value is the next fizz value except if the fizz value is divisible by 5 then it should return the string buzz (You will need to call the inherited next() method as well as look at the inherited value of number)
    '''

    def __init__(self, number, start= 0):
        super().__init__(self)
        self.number = number

           
    def next(self):
        #first call the next() method from the parent class
        n = super().next() 
        
        if (self.number % 5 == 0):
            return "buzz"
        elif (self.number % 3) == 0:
            return n
        else:
            return str(self.number)
        
        return n

buzzer = Buzz(11)
assert buzzer.next() == "fizz"
assert buzzer.next() == "13"
assert buzzer.next() == "14"
assert buzzer.next() == "buzz"
