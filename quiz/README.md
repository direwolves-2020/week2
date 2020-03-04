
## Quiz: FizzBuzzer class

### Part 1

* Create a class called Fizz

* It has a constructor that takes in an argument, `start` whose default value is 0. 
It also has an integer instance property called `number` that is set to equal `start`

* It has an instance method called `next` that takes no arguments. 
This method increases the value of `number` by 1 and then returns a string of that number's fizz value.

The fizz value of n = "fizz" if n is evenly divisible by 3. If n is not divisible by 3 then the fizz value is the value of n converted into a string.

Example

```py
buzzer = FizzBuzzer(11)
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
```

outputs

```
fizz
13
14
```

* Now create a class `Buzz` that is a subclass of `Fizz`.

* It should have a constructor like `Fizz` where it takes in an argument `start` with a default value of 0 but it should not have any instance variable of its own. Instead it should rely on the inherited class `Fizz`'s `number` value (which will require you to invoke the constructor of the base class `Fizz` from `Buzz`'s constructor).

* `Buzz` should have a method `next` which should return the next buzz value. The buzz value is the next fizz value except if the fizz value is divisible by 5 then it should return the string `buzz` (You will need to call the inherited `next()` method as well as look at the inherited value of `number`)

and 

```py
buzzer = Buzzer(11)
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
```

produces

```
fizz
13
14
buzz
```

Make sure to add assert statements to verify the output of your code

### Part 2 - Searching and Sorting

#### BST

Explain in your own words why BST is more efficient O(log n) time for insertion/search tasks than linear data structures (arrays/lists) that take O(n) time. 

#### QuickSort vs MergeSort

Explain why bubblesort is O(n^2), while mergesort is O(log n). 

### Open book, open notes

* You are free to use Google & look at your code from class. 