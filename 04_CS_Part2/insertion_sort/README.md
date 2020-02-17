# Insertion Sort

#### Algorithm

Insertion sort is a common sorting algorithm that, while still its worst case is still O(n**2), it is much more efficient than Bubble sort on average.

According to wikipedia, when people manually sort something, like a deck of cards for example, most use a method similar to insertion sort.

The algorithm is simple - here it is in pseudocode.
```
from i = 1 to length of array:
    j = i
    while j > 0 and array[j-1] > array[j]:
        swap array[j] and array[j-1]
        j = j - 1
```

#### Objectives

* Write a function `insertion_sort()`
* This function will take an unsorted `list` as an argument
* This function will return a sorted `list` using the insertion sort algorithm
* Try pseudo coding this first before actually coding

#### REQUIRED Reading and Watching

* [https://study.cs50.net/insertion_sort](https://study.cs50.net/insertion_sort)