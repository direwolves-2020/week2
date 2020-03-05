class Fizz:
    def __init__(self, start = 0):
        self.start = start
        self.number = start
        self.value = 0

    def fizzcheck(self):
        if self.number %3 == 0:
            self.value = 'Fizz'
        else: self.value = self.number
        

    def next(self):
        self.number += 1
        self.fizzcheck()
        return self.value

class Buzz(Fizz):
    def __init__(self, start):
        Fizz.__init__(self, start)

    #buzz does whhat fizz does plus a little more 
    def buzzcheck(self):
        super(Buzz, self).fizzcheck()
        if self.number %5 == 0:
            self.value = 'Buzz'
        return self.value
        
    def next(self):
        self.number += 1
        return self.buzzcheck()


fizz_test = Fizz(14)
buzz_test = Buzz(14)

assert fizz_test.next() == 'Fizz', "Fizz only?"
assert buzz_test.next() == "Buzz", "Buzz override"

fizz_test = Fizz(11)
buzz_test = Buzz(11)

assert fizz_test.next() == 'Fizz', "Fizz only"
assert buzz_test.next() == "Fizz", "No buzz here"

fizz_test = Fizz(10)
buzz_test = Buzz(10)

assert fizz_test.next() == 11, "neither fizz nor buzz"
assert buzz_test.next() == 11, "neither fizz nor buzz"



