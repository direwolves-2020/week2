class Fizz: 
#initializing class with start and number, couldn't set number = start so I just reset the instance number within the block. 
    def __init__(self, start=0, number=0): 
        self.start = start
        self.number = start
#Tracking the incrementing number/fizz values
    def next(self): 
        self.number += 1 
        if self.number % 3 == 0:
            return "Fizz"
        elif self.number % 3 != 0: 
            return str(self.number)
        

class Buzz(Fizz): 

    def __init__(self, start=0, number=0): 
        Fizz.__init__(self, start, number)

#Calling next from parent class and storing return in val - only returning if number is not divisible by 5
    def next(self):
        val = Fizz.next(self)
        if self.number % 5 == 0: 
            return "Buzz"
        else: 
            return val


buzzer = Buzz(11)
assert buzzer.next() == "Fizz"
assert buzzer.next() == "13"

buzzer = Buzz(14)
assert buzzer.next() == "Buzz"
assert buzzer.next() == "16"

buzzer = Buzz(433)
assert buzzer.next() == "434"
assert buzzer.next() == "Buzz"

buzzer = Buzz(563)
assert buzzer.next() == "Fizz"
assert buzzer.next() == "Buzz"
 
"""
Answer to essay question: 
O(log n) is a much more effecient way to sort/insert data when compared to O(n). With O(n) the program will have to go through each 
element in a list at least one time. For an example, lets say our list is [1, 5, 7, 6, 3, 8, 9]. If this is searched using O(n), then
each element has to be processed. However, if this were a binary search tree with 7 as the Root and the user is searching for 9, then 
immediately any value below seven does not need to be processed. This would mean that 4 elements would no longer need to be processed. 
Finding 9 would only require 2 sorts to find 9 compared to O(n) which would require 7, one for each element of the list. 

Bubble sort evaluates two inputs each pass through a list, and will loop through a list multiple times until all elements are in proper
order, evaluating elements multiple times is what makes it O(n^2). Merge sort takes an array and splits it in two halves, and then recursively
works through each half until the sorted array at hand only has one element, it then merges. This process splits the array and then 
takes linear time to merge elements back together to create the sorted array, making it O(log n).
"""